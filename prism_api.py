"""Prism contracts verified from the project's live OpenAPI document and SDK 0.5.1."""
import json
import os
import ssl
import urllib.request
import urllib.error
from urllib.parse import urlencode
from integrations import load_env


class SponsorError(RuntimeError):
    pass


def request(path, payload=None, method=None, timeout=10):
    load_env()
    host = os.environ.get('PRISMTRACE_HOST', '').rstrip('/')
    if host not in ('https://prism.blockconvey.com', 'https://prism-api-prod.up.railway.app'):
        raise SponsorError('Configure the verified Prism host.')
    key = os.environ.get('PRISMTRACE_API_KEY')
    if not key:
        raise SponsorError('Prism key is missing from .env.')
    body = None if payload is None else json.dumps(payload, allow_nan=False).encode()
    req = urllib.request.Request(host + path, data=body, method=method,
        headers={'Content-Type': 'application/json', 'X-PRISMtrace-Key': key})
    context = ssl.create_default_context()
    if os.path.isfile('/etc/ssl/cert.pem'):
        context.load_verify_locations('/etc/ssl/cert.pem')
    try:
        with urllib.request.urlopen(req, timeout=timeout, context=context) as r:
            result = r.read().decode()
    except urllib.error.HTTPError as e:
        detail = e.read().decode(errors='replace').replace(key, '[REDACTED]')
        raise SponsorError(f'Prism HTTP {e.code}: {detail[:600]}') from None
    except (urllib.error.URLError, TimeoutError):
        raise SponsorError('Prism is unreachable or timed out; verification is incomplete.') from None
    return json.loads(result.replace(key, '[REDACTED]'))


def project_query(**extra):
    load_env()
    return urlencode({'project_id': os.environ['PRISMTRACE_PROJECT_ID'], **extra})
