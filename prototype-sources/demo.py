#!/usr/bin/env python3
"""Génération statique de démonstration, à partir des seules fixtures locales."""
import html
import json
import sys
from pathlib import Path
from instagram import normalize as normalize_instagram
from spectacles import normalize as normalize_spectacles

ROOT = Path(__file__).resolve().parent

def render(posts, shows):
    esc = lambda value: html.escape(str(value), quote=True)
    p = ''.join('<li><a href="{}">{}</a> — {}</li>'.format(esc(x['lien']), esc(x['texte'] or 'Voir la publication'), esc(x['date'])) for x in posts)
    s = ''.join('<li><a href="{}">{}</a></li>'.format(esc(x['url']), esc(x['titre_source'])) for x in shows)
    return '''<!doctype html><html lang="fr"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Démonstration des sources</title><style>body{{font:18px/1.5 system-ui;margin:2rem auto;padding:0 1rem;max-width:48rem;background:#171720;color:#fff}}a{{color:#9edbff}}li{{margin:1rem 0}}.notice{{background:#483927;padding:1rem}}</style><h1>Démonstration des sources</h1><p class="notice">Simulation : données Instagram fictives et titres Linktree relevés manuellement. Aucune mise à jour réelle.</p><h2>Publications Instagram</h2><ul>{}</ul><h2>Spectacles</h2><ul>{}</ul></html>'''.format(p or '<li>Aucune publication.</li>', s or '<li>Aucun spectacle.</li>')

def main(out):
    out.mkdir(parents=True, exist_ok=False)
    posts = normalize_instagram(json.loads((ROOT/'fixtures/instagram.json').read_text(encoding='utf-8')))
    shows = normalize_spectacles(json.loads((ROOT/'fixtures/spectacles.json').read_text(encoding='utf-8')))
    for name, value in [('instagram.json', posts), ('spectacles.json', shows)]:
        (out/name).write_text(json.dumps(value, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    (out/'index.html').write_text(render(posts['posts'], shows['spectacles']), encoding='utf-8')

if __name__ == '__main__':
    main(Path(sys.argv[1]))
