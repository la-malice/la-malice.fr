#!/usr/bin/env python3
"""Essai ponctuel du profil public ; sortie réservée au spike, pas au site."""
import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit
from urllib.request import Request, urlopen

URL = 'https://linktr.ee/lamaliceimprovise'
MAX_BYTES = 2_000_000
DATE_PREFIX = re.compile(r'^\s*\d{1,2}\s+(?:janv|fév|fev|mars|avr|mai|juin|juil|août|aout|sept|oct|nov|déc|dec)', re.I)

class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.buttons = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'a' and attrs.get('data-testid') == 'LinkClickTriggerLink':
            self.buttons.append((attrs.get('aria-label', ''), attrs.get('href', '')))

def parse(text):
    parser = Links()
    parser.feed(text)
    if not parser.buttons:
        raise ValueError('aucun bouton reconnu : structure ou réponse inattendue')
    events = []
    for title, url in parser.buttons:
        if not DATE_PREFIX.match(title):
            continue
        parsed = urlsplit(url)
        if parsed.scheme != 'https' or not parsed.hostname or parsed.username or parsed.password:
            raise ValueError('lien de spectacle invalide')
        events.append({'titre': title, 'url': url})
    return events

def fetch():
    request = Request(URL, headers={'User-Agent': 'LaMaliceSpike/1.0'})
    with urlopen(request, timeout=20) as response:
        if urlsplit(response.geturl()).hostname != 'linktr.ee':
            raise ValueError('redirection inattendue')
        if response.headers.get_content_type() != 'text/html':
            raise ValueError('réponse non HTML')
        body = response.read(MAX_BYTES + 1)
        if len(body) > MAX_BYTES:
            raise ValueError('réponse trop volumineuse')
        return parse(body.decode('utf-8'))

if __name__ == '__main__':
    try:
        events = fetch()
        Path(sys.argv[1]).write_text(json.dumps(events, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
        print(f'{len(events)} lien(s) de spectacle repéré(s) ; vérifier les intitulés.')
    except Exception as exc:
        sys.exit('Collecte Linktree impossible : ' + type(exc).__name__)
