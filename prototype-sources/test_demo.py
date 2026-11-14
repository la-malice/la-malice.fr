import unittest
from demo import render
from instagram import normalize as posts
from spectacles import normalize as shows
from ia_spectacles import validate

class DemoTest(unittest.TestCase):
    def test_empty_is_valid(self):
        self.assertEqual(posts({'data': []})['posts'], [])
        self.assertEqual(shows([])['spectacles'], [])
        self.assertIn('Aucune publication.', render([], []))
    def test_invalid_is_not_empty(self):
        with self.assertRaises(ValueError):
            posts({'data': None})
    def test_source_text_is_escaped(self):
        result = render([], [{'url':'https://example.org','titre_source':'<script>'}])
        self.assertNotIn('<script>', result)
        self.assertIn('&lt;script&gt;', result)
    def test_ai_cannot_invent_year(self):
        entries = [{'titre':'20 Nov. Retrouvailles', 'url':'https://example.org'}]
        result = {'spectacles':[{'titre_source':entries[0]['titre'],'url':entries[0]['url'],'date':'2026-11-20','lieu':None}]}
        with self.assertRaises(ValueError):
            validate(entries, result)

if __name__ == '__main__':
    unittest.main()
