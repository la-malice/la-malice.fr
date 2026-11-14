#!/usr/bin/env python3
"""Exemple local sans appel réseau : les dates ambiguës restent inconnues."""
import json
import sys
from pathlib import Path
from urllib.parse import urlsplit

def normalize(links):
    if not isinstance(links, list):
        raise ValueError('liste attendue')
    result = []
    for entry in links:
        title, url = entry['titre'], entry['url']
        if not isinstance(title, str) or not title.strip() or urlsplit(url).scheme != 'https':
            raise ValueError('titre ou lien invalide')
        result.append({'titre_source': title, 'url': url, 'date': None, 'lieu': None})
    return {'simulation': True, 'spectacles': result}

if __name__ == '__main__':
    try:
        result = normalize(json.loads(Path(sys.argv[1]).read_text()))
        Path(sys.argv[2]).write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    except (ValueError, KeyError, TypeError, OSError, IndexError) as exc:
        sys.exit(f'Erreur spectacles : {exc}')
