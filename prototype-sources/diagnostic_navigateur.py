#!/usr/bin/env python3
"""Diagnostic unique sans authentification : observe les liens du profil rendu."""
import json
import html
import re
import shutil
import subprocess
import sys
import tempfile
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit

class PostLinks(HTMLParser):
    def __init__(self):
        super().__init__()
        self.urls = set()
    def handle_starttag(self, tag, attrs):
        if tag != 'a':
            return
        href = dict(attrs).get('href', '')
        parsed = urlsplit(href)
        if parsed.netloc and parsed.hostname not in ('www.instagram.com', 'instagram.com'):
            return
        if re.fullmatch(r'/(?:lamaliceimprovise/)?(?:p|reel)/[A-Za-z0-9_-]+/?', parsed.path):
            self.urls.add('https://www.instagram.com' + parsed.path)

def main(output):
    chrome = next((shutil.which(name) for name in ('google-chrome', 'chromium', 'chromium-browser') if shutil.which(name)), None)
    if not chrome:
        raise RuntimeError('Chrome ou Chromium indisponible')
    with tempfile.TemporaryDirectory(prefix='instagram-spike-') as profile:
        run = subprocess.run([chrome, '--headless', '--no-sandbox', '--disable-gpu', '--disable-dev-shm-usage', '--no-first-run', '--user-data-dir='+profile, '--virtual-time-budget=15000', '--dump-dom', 'https://www.instagram.com/lamaliceimprovise/'], capture_output=True, text=True, timeout=75)
    parser = PostLinks()
    parser.feed(run.stdout)
    match = re.search(r'<title[^>]*>(.*?)</title>', run.stdout, re.I | re.S)
    title = html.unescape(re.sub(r'\s+', ' ', match.group(1)).strip())[:200] if match else None
    summary = {'source': 'profil public non connecté', 'code_navigateur': run.returncode, 'titre_page': title, 'taille_dom_octets': len(run.stdout.encode('utf-8')), 'contient_identifiant_profil': 'lamaliceimprovise' in run.stdout.lower(), 'liens_publications': sorted(parser.urls), 'nombre_liens': len(parser.urls), 'statut': 'liens_detectes' if parser.urls else 'aucun_lien_detecte'}
    Path(output).write_text(json.dumps(summary, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    print('Liens de publications détectés :', len(parser.urls), '; code navigateur :', run.returncode)
    if run.returncode != 0 or not parser.urls:
        sys.exit(1)

if __name__ == '__main__':
    main(sys.argv[1])
