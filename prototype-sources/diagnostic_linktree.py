#!/usr/bin/env python3
"""Code et quelques en-têtes publics uniquement ; aucun secret ni corps conservé."""
import json
import sys
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

request = Request('https://linktr.ee/lamaliceimprovise', headers={'User-Agent': 'LaMaliceSpike/1.0'})
try:
    response = urlopen(request, timeout=20)
except HTTPError as exc:
    response = exc
except URLError as exc:
    print('Erreur réseau :', type(exc.reason).__name__)
    sys.exit(1)
with response:
    result = {'status': response.status, 'headers': {k: response.headers.get(k) for k in ('Server', 'Content-Type', 'CF-Ray') if response.headers.get(k)}}
Path(sys.argv[1]).write_text(json.dumps(result, indent=2)+'\n')
print('Linktree HTTP', result['status'], '; serveur :', result['headers'].get('Server', 'non précisé'))
