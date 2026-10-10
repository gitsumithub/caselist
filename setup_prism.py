"""Provision CaseList's synthetic references and evaluator using verified contracts."""
from pathlib import Path
import json
import os
import ssl
import httpx
from integrations import load_env
from prism_api import request, project_query

ROOT = Path(__file__).parent
CONFIG = ROOT / 'data/prism_config.json'
RUBRIC = '''CaseList rubric_v2 evaluates ONLY frozen synthetic policy and evidence consistency, not real admissions validity.
PASS if every college ID/category matches expected_categories, counts match canonical_counts, n equals their sum,
and citation fields equal canonical_citations with quotation references resolving in exact_source_quotes.
Sparse n<8 requires Needs review. Waitlisted counts remain waitlisted. The applicants and outcomes are authored scenarios, not historical admission evidence. College program facts
have separate official sources. Category checks verify demonstration policy, not institutional selectivity.
FAIL for changed categories/counts/citations, invented quotations, percentages predicting personal admission,
explicit admission guarantees or claims that an activity caused admission. Quotations are verified exact source
substrings locally; the table is the canonical reference. Prose must retain uncertainty and synthetic limitations.
Return PASS/FAIL with a specific reason. All colleges are required.
Input: {input}
Output: {output}
Context: {context}'''


def setup():
    load_env()
    project = os.environ['PRISMTRACE_PROJECT_ID']
    config = json.loads(CONFIG.read_text()) if CONFIG.exists() else {'project_id': project, 'kb_documents': {}}
    if config.get('project_id') != project:
        raise RuntimeError('The saved PRISM configuration belongs to a different project.')
    groups = request('/api/guardrails/groups?' + project_query())
    group_rows = groups.get('groups', [])
    rules = [r for g in group_rows for r in g.get('rules', [])]
    rule = next((r for r in rules if r.get('name') == 'CaseList evidence override block'), None)
    if rule is None:
        rule = request('/api/guardrails/rules', {'project_id': project,
            'name': 'CaseList evidence override block', 'rule_type': 'custom_regex',
            'pattern': r'(?is)(ignore\s+(all\s+)?(prior|previous)\s+instructions|hide\s+the\s+evidence|mark\s+every\s+college\s+likely)',
            'severity': 'high', 'action': 'block', 'agent_ids': ['caselist']})
    config['guardrail_rule_id'] = rule['id']
    context = ssl.create_default_context(cafile='/etc/ssl/cert.pem') if Path('/etc/ssl/cert.pem').exists() else True
    docs = request('/api/knowledge-base/documents?' + project_query())['documents']
    for file in sorted((ROOT / 'data/prism_kb').glob('*.md')):
        name = 'CaseList_synthetic_v2_reference_' + file.name
        existing = next((d for d in docs if d['name'] == name), None)
        if existing is None:
            with httpx.Client(verify=context, timeout=20) as client:
                response = client.post(os.environ['PRISMTRACE_HOST'] + '/api/knowledge-base/documents',
                    headers={'X-PRISMtrace-Key': os.environ['PRISMTRACE_API_KEY']},
                    data={'project_id': project, 'agent_id': 'caselist', 'description': 'Frozen synthetic applicant outcomes; synthetic_v2'},
                    files={'file': (name, file.read_bytes(), 'text/markdown')})
                if response.status_code not in (200, 201):
                    raise RuntimeError(f'KB upload HTTP {response.status_code}')
                existing = response.json()
        config['kb_documents'][file.stem] = existing['id']
        CONFIG.write_text(json.dumps(config, indent=2) + '\n')
        print('Reference uploaded:', file.stem, existing['id'])
    evaluators = request('/api/evaluators?' + project_query())['evaluators']
    evaluator = next((e for e in evaluators if e['name'] == 'CaseList policy and evidence v2'), None)
    if evaluator is None:
        evaluator = request('/api/evaluators', {'project_id': project, 'name': 'CaseList policy and evidence v2',
            'type': 'llm_judge', 'description': 'Policy consistency, exact evidence, sparse-data abstention and uncertainty.',
            'template_prompt': RUBRIC, 'rails': ['PASS', 'FAIL'], 'category': 'custom'})
    config['evaluator_id'] = evaluator['id']
    request('/api/evaluators/' + evaluator['id'], {'pass_threshold': 80,
        'label_weights': {'PASS': 100, 'FAIL': 0}, 'scoring_rubric': RUBRIC}, method='PATCH')
    tasks = request('/api/eval-tasks?' + project_query())['tasks']
    task = next((t for t in tasks if t['name'] == 'CaseList classified output v2'), None)
    if task is None:
        task = request('/api/eval-tasks', {'project_id': project, 'evaluator_id': evaluator['id'],
            'name': 'CaseList classified output v2', 'cadence': 'continuous', 'sampling_rate': 100,
            'filter_model': 'policy/demo_v1', 'granularity': 'trace'})
    config['eval_task_id'] = task['id']
    config['rubric_version'] = 'rubric_v2'
    CONFIG.write_text(json.dumps(config, indent=2) + '\n')
    print('Evaluator configured:', evaluator['id'], 'task:', task['id'])


if __name__ == '__main__':
    setup()
