#!/usr/bin/env python3
"""Essai ponctuel du profil public ; sortie réservée au spike, pas au site."""
import base64
import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit
from urllib.error import HTTPError
from urllib.request import Request, urlopen

URL = 'https://linktr.ee/lamaliceimprovise'
MAX_BYTES = 2_000_000
DATE_PREFIX = re.compile(r'^\s*\d{1,2}\s+(?:janv|fév|fev|mars|avr|mai|juin|juil|août|aout|sept|oct|nov|déc|dec)', re.I)

class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.buttons = []
        self.page_data = []
        self.in_page_data = False

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'script' and attrs.get('id') == '__NEXT_DATA__':
            self.in_page_data = True
        if tag == 'a' and attrs.get('data-testid') == 'LinkClickTriggerLink':
            self.buttons.append((attrs.get('aria-label', ''), attrs.get('href', '')))

    def handle_endtag(self, tag):
        if tag == 'script':
            self.in_page_data = False

    def handle_data(self, data):
        if self.in_page_data:
            self.page_data.append(data)


def parse(text):
    parser = Links()
    parser.feed(text)
    if not parser.buttons:
        raise ValueError('aucun bouton reconnu : structure ou réponse inattendue')
    page = json.loads(''.join(parser.page_data)) if parser.page_data else {}
    links = page.get('props', {}).get('pageProps', {}).get('links', [])
    metadata = {(link.get('title'), link.get('url')): link for link in links}
    events = []
    for title, url in parser.buttons:
        if not DATE_PREFIX.match(title):
            continue
        parsed = urlsplit(url)
        if parsed.scheme != 'https' or not parsed.hostname or parsed.username or parsed.password:
            raise ValueError('lien de spectacle invalide')
        event = {'titre': title, 'url': url}
        link = metadata.get((title, url), {})
        preview = link.get('metaData') or {}
        for field, value in (
            ('titre_partage', preview.get('ogTitle') or preview.get('title')),
            ('description_partage', preview.get('ogDescription') or preview.get('description')),
            ('miniature_source', link.get('thumbnail')),
        ):
            if isinstance(value, str) and value.strip():
                event[field] = value.strip()
        events.append(event)
    return events

def thumbnail(url):
    parsed = urlsplit(url)
    host = 'ugc.production.linktr.ee'
    if parsed.scheme != 'https' or parsed.netloc != host or parsed.query or parsed.fragment:
        raise ValueError('Adresse de vignette Linktree inattendue')
    request = Request(url + '?io=true&size=thumbnail-stack_v1_0')
    with urlopen(request, timeout=20) as response:
        if urlsplit(response.geturl()).netloc != host:
            raise ValueError('Redirection de vignette inattendue')
        mime = response.headers.get_content_type()
        image = response.read(MAX_BYTES + 1)
    if mime not in ('image/jpeg', 'image/png', 'image/webp') or not 0 < len(image) <= MAX_BYTES:
        raise ValueError('Vignette Linktree invalide')
    return f'data:{mime};base64,' + base64.b64encode(image).decode('ascii')


def fetch(*, include_images=False):
    request = Request(URL, headers={'User-Agent': 'LaMaliceSpike/1.0'})
    with urlopen(request, timeout=20) as response:
        if urlsplit(response.geturl()).hostname != 'linktr.ee':
            raise ValueError('redirection inattendue')
        if response.headers.get_content_type() != 'text/html':
            raise ValueError('réponse non HTML')
        body = response.read(MAX_BYTES + 1)
        if len(body) > MAX_BYTES:
            raise ValueError('réponse trop volumineuse')
    events = parse(body.decode('utf-8'))
    for event in events:
        source = event.pop('miniature_source', None)
        if include_images and source:
            event['image'] = thumbnail(source)
    return events

if __name__ == '__main__':
    try:
        events = fetch()
        Path(sys.argv[1]).write_text(json.dumps(events, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
        print(f'{len(events)} lien(s) de spectacle repéré(s) ; vérifier les intitulés.')
    except HTTPError as exc:
        sys.exit(f'Collecte Linktree impossible : HTTP {exc.code}')
    except Exception as exc:
        sys.exit('Collecte Linktree impossible : ' + type(exc).__name__)
