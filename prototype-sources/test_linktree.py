import unittest
from linktree import parse

class LinktreeTest(unittest.TestCase):
    def test_events_and_other_links(self):
        html = '<a data-testid="LinkClickTriggerLink" aria-label="20 Nov. Concert - TARNOS" href="https://example.org/a"></a><a data-testid="LinkClickTriggerLink" aria-label="Site" href="https://example.org/"></a>'
        self.assertEqual(parse(html), [{'titre':'20 Nov. Concert - TARNOS','url':'https://example.org/a'}])
    def test_changed_structure_is_error(self):
        with self.assertRaises(ValueError):
            parse('<html></html>')
    def test_empty_events(self):
        self.assertEqual(parse('<a data-testid="LinkClickTriggerLink" aria-label="Site" href="https://example.org"></a>'), [])
    def test_reject_insecure_url(self):
        with self.assertRaises(ValueError):
            parse('<a data-testid="LinkClickTriggerLink" aria-label="12 Déc. Match" href="http://example.org/"></a>')

if __name__ == '__main__':
    unittest.main()
