"""Authored scenario enrichment; outcomes remain explicit policy fixtures."""
from pathlib import Path
import json
import random
def scenario_names():
    """Stable random pairings of fictional labels; never used in matching."""
    first = ['Amelia', 'Noah', 'Olivia', 'Liam', 'Sophia', 'Elijah', 'Charlotte', 'James', 'Isabella', 'Lucas', 'Mia', 'Mason', 'Evelyn', 'Ethan', 'Harper', 'Aiden', 'Abigail', 'Henry', 'Emily', 'Jackson', 'Elizabeth', 'Sebastian', 'Avery', 'Jack', 'Sofia', 'Owen', 'Ella', 'Samuel', 'Madison', 'Matthew', 'Scarlett', 'Joseph', 'Victoria', 'Levi', 'Aria', 'David', 'Grace', 'Daniel', 'Chloe', 'Carter', 'Camila', 'Wyatt', 'Penelope', 'Jayden', 'Riley', 'Julian', 'Layla', 'Luke', 'Lillian', 'Gabriel', 'Nora', 'Isaac', 'Zoey', 'Anthony', 'Hannah', 'Dylan', 'Addison', 'Leo', 'Audrey', 'Caleb']
    last = ['Rivera', 'Park', 'Bennett', 'Shah', 'Morgan', 'Ali', 'Chen', 'Patel', 'Thompson', 'Garcia', 'Williams', 'Nguyen', 'Anderson', 'Martinez', 'Wilson', 'Brown', 'Davis', 'Rodriguez', 'Lee', 'Walker', 'Hall', 'Allen', 'Young', 'Hernandez', 'King', 'Wright', 'Lopez', 'Hill', 'Scott', 'Green', 'Adams', 'Baker', 'Nelson', 'Carter', 'Mitchell', 'Perez', 'Roberts', 'Turner', 'Phillips', 'Campbell', 'Evans', 'Edwards', 'Collins', 'Stewart', 'Sanchez', 'Morris', 'Rogers', 'Reed', 'Cook', 'Bell', 'Murphy', 'Bailey', 'Cooper', 'Richardson', 'Cox', 'Howard', 'Ward', 'Torres', 'Peterson', 'Gray']
    rng = random.Random(20261010)
    rng.shuffle(first)
    rng.shuffle(last)
    return [a + ' ' + b for a, b in zip(first, last)]

def enrich():
    r=Path(__file__).parent; d=json.loads((r/'data/dataset.json').read_text())
    projects=[
    ('robotics sensor calibration','Built a calibration log for the robotics team and tutored two beginners through sensor tests.','A wheel encoder counted turns while the robot stood still. I recorded ten trials before blaming the code.','I learned that explaining a failed test can help a team more than presenting a perfect result.'),
    ('library coding workshop','Ran a library programming workshop using paper algorithms before introducing Python.','A participant could follow my code but could not explain the loop. I replaced the screen with numbered cards.','Teaching made me notice the assumptions I had hidden inside my own explanations.'),
    ('accessible club website','Redesigned the robotics club website for keyboard navigation and coached classmates in HTML.','Our event form trapped keyboard users inside a menu. I asked a classmate to test without a mouse.','I began treating accessibility as a design requirement rather than a final checklist.'),
    ('food pantry inventory','Wrote a small inventory tool for a food pantry and taught volunteers how to check its totals.','Two volunteers entered the same delivery. I added a receipt identifier and a visible correction history.','A useful program must let people recognize and repair its mistakes.'),
    ('robotics team documentation','Created a troubleshooting notebook for the robotics team and hosted lunchtime debugging sessions.','The senior programmer graduated with the only working setup on a laptop. I rebuilt the instructions on a clean machine.','Documentation became a way to include teammates who were afraid to ask basic questions.'),
    ('water monitoring project','Logged readings from a school water sensor and taught younger robotics members to plot measurements.','One dramatic spike disappeared when we cleaned a loose connector. I kept the original reading beside the corrected one.','I learned to question attractive conclusions when the measurement process was uncertain.'),
    ('peer tutoring scheduler','Built a peer tutoring signup tool and helped the robotics team organize practice sessions.','My first schedule assigned a tutor during their own class. I interviewed users before rewriting the time rules.','Listening to the people affected by my code changed what I considered a successful solution.'),
    ('repair cafe diagnostic guide','Volunteered at a repair cafe, prototyped a robotics diagnostic guide and tutored introductory programming.','A donated laptop would not charge. I checked the cable before opening the case and wrote down each test.','Small, reversible tests helped me explain technical work without pretending I already knew the answer.')]
    names = scenario_names()
    settings=['after school','at a Saturday workshop','during our spring showcase','with a new club member','before a community open house','during a summer volunteer session','in a lunchtime study group','while preparing a handover to next year’s team']
    for i,p in enumerate(d['applicants']):
        title,activity,incident,reflection=projects[i%8]
        p['name']=names[i]
        p['synthetic']=True
        p['project']=title
        p['activities']=activity+f" Worked {2+i%5} hours per week for {12+i%17} weeks; balanced the project with "+['a weekend grocery shift.','school orchestra rehearsals.','caring for a younger sibling.','cross-country practice.','debate club meetings.','a school newspaper role.'][i%6]
        p['essay']=incident+' This happened '+settings[(i//8+i)%8]+'. '+reflection+' My next step was '+['to write a checklist another student could test.','to ask a beginner to explain the result back to me.','to keep a notebook of failed attempts as well as working ones.','to make the instructions usable without my help.','to compare two approaches before choosing one.','to admit which part of the result I could not yet explain.','to leave time for another person to challenge my assumptions.','to organize a short practice session instead of adding more features.'][(i//8)%8]
        p['courses']=(['AP Computer Science A','AP Calculus AB','AP Physics 1','AP English Language'] if p['rigor']==2 else ['AP Computer Science Principles','Honors Precalculus','English 11','Physics'] if p['rigor']==1 else ['Algebra II','English 11','Biology','Introductory Computing'])
        p['provenance']='Authored synthetic scenario; profile and application decisions are not historical records.'
        p['activity_tags']=['robotics','peer_tutoring']
    refs=[
    ('Stony Brook University','https://www.stonybrook.edu/academics/majors-minors-and-programs/','Computer Science B.S. appears in the university program directory.'),
    ('University at Buffalo','https://engineering.buffalo.edu/computer-science-engineering/undergraduate/degrees-and-programs/bs-in-computer-science.html','The university offers a B.S. in Computer Science.'),
    ('The City College of New York','https://www.ccny.cuny.edu/compsci/admissions','Computer Science undergraduate admissions are handled centrally; Grove School has additional requirements.'),
    ('Queens College','https://www.qc.cuny.edu/academics/cs/undergraduate-studies/','The department publishes undergraduate Computer Science study options.'),
    ('Brooklyn College','https://www.brooklyn.edu/academics/programs/computer-science-bs/','The college offers a B.S. in Computer Science.'),
    ('Binghamton University','https://www.binghamton.edu/computer-science/undergraduate-programs/','The department publishes undergraduate Computer Science programs.')]
    for c,(name,url,fact) in zip(d['colleges'],refs):
        c.update(name=name,fictional=False,reference={'claim':fact,'url':url,'checked_on':'2026-10-10','type':'Official college program information'},outcome_scope='Illustrative scenario outcomes, not this college’s historical admission record')
    for a in d['applications']: a['provenance']='Authored scenario decision; no causal explanation or empirical admission rate is implied.'
    d['version']='synthetic_v2';d['provenance']={'applicants':'60 authored scenarios with unique essays and activities','outcomes':'Designed fixtures for policy branches, sparse evidence and unresolved waitlists; not sampled admission results','college_facts':'Official program pages checked October 10, 2026','limitation':'Names of real institutions do not make generated outcomes empirical. This prototype cannot validate real-outcome predictions.'}
    (r/'data/dataset.json').write_text(json.dumps(d,indent=2)+'\n')
    by={p['applicant_id']:p for p in d['applicants']}
    for c in d['colleges']:
        lines=[f"# {c['name']} | {c['college_id']}",'SYNTHETIC DEMONSTRATION DATA. Dataset synthetic_v2. Not real admissions outcomes.',f"Official program reference: {c['reference']['claim']} Source: {c['reference']['url']}. Checked: 2026-10-10.",'']
        for a in d['applications']:
            if a['college_id']!=c['college_id']:continue
            p=by[a['applicant_id']]
            lines.extend([f"## {a['application_id']} | {p['applicant_id']}",f"College: {c['college_id']}; cycle: {a['cycle']}; round: regular; outcome: {a['outcome']}.",f"Unweighted GPA: {p['gpa']}/4.0. Rigor level: {p['rigor']}.",f"Courses: {', '.join(p['courses'])}.",f"Activities: {p['activities']}",f"Essay: {p['essay']}",''])
        (r/f"data/prism_kb/{c['college_id']}.md").write_text('\n'.join(lines))
