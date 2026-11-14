import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from apercu_sources import render


class PreviewTest(unittest.TestCase):
    def test_undated_titles_and_unsupported_fields(self):
        links = [
            {'titre': 'Cabaret d’impro', 'description_partage': 'Le 4 avril au Microphone.'},
            {'titre': '12 avril — Cours de théâtre'},
            {'titre': 'En savoir plus'},
            {'titre': 'Spectacle surprise'},
        ]
        base = dict(titre=None, date=None, heure=None, format=None, salle=None, ville=None)
        answers = [
            dict(base, categorie='spectacle', titre='Cabaret d’impro', date='2027-04-04',
                 heure='20:30', salle='Microphone', ville='Paris'),
            dict(base, categorie='autre'),
            dict(base, categorie='incertain'),
            dict(base, categorie='spectacle', date='2027-02-31'),
        ]
        with tempfile.TemporaryDirectory() as folder:
            output = Path(folder) / 'index.html'
            with patch('apercu_sources.synthesize', side_effect=answers):
                render({'spectacles': links, 'instagram': []},
                       '<head></head><article class="panel event">Ancienne carte</article>', output)
            html = output.read_text()
            shows = json.loads(output.with_name('spectacles.json').read_text())
            review = json.loads(output.with_name('spectacles-a-verifier.json').read_text())
        self.assertEqual([show['titre'] for show in shows], ['Cabaret d’impro', 'Spectacle surprise'])
        self.assertEqual(shows[0]['date'], '--04-04')
        self.assertEqual(shows[0]['salle'], 'Microphone')
        for field in ('heure', 'ville', 'url'):
            self.assertIsNone(shows[0][field])
        self.assertIsNone(shows[1]['date'])
        self.assertEqual(review, [{'titre': 'En savoir plus', 'url': None}])
        self.assertIn('4 avril', html)
        self.assertNotIn('Réserver', html)
        self.assertNotIn('Cours de théâtre', html)
