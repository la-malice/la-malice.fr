#!/usr/bin/env python3
"""Normalisation hors ligne du contrat simulé du prototype Instagram."""
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlsplit

def normalize(data):
    if not isinstance(data.get('data'), list):
        raise ValueError('liste data absente')
    posts = []
    for p in data['data']:
        image = p.get('thumbnail_url') if p.get('media_type') == 'VIDEO' else p.get('media_url')
        link = p.get('permalink', '')
        if not image or urlsplit(image).scheme != 'https' or urlsplit(link).hostname not in ('instagram.com', 'www.instagram.com'):
            raise ValueError('publication inexploitable')
        date = datetime.fromisoformat(p['timestamp'].replace('Z', '+00:00'))
        if date.tzinfo is None:
            raise ValueError('date sans fuseau')
        posts.append({'image': image, 'lien': link, 'texte': p.get('caption', ''), 'date': date.astimezone(timezone.utc).isoformat()})
    posts.sort(key=lambda p: p['date'], reverse=True)
    return {'simulation': True, 'posts': posts[:6]}

if __name__ == '__main__':
    try:
        result = normalize(json.loads(Path(sys.argv[1]).read_text()))
        Path(sys.argv[2]).write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    except (ValueError, KeyError, TypeError, OSError, IndexError) as exc:
        sys.exit(f'Erreur Instagram : {exc}')
