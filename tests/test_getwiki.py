import unittest
from getwiki import get_wiki


class TestFirestore(unittest.TestCase):

    def test_get_wiki(self):
        languages = ["en", "de", "fr", "sv", "ja", "zh"]
        wikis = {}
        for language in languages:
            img, text = get_wiki(language)
            wikis[language] = (img, text)
        output = True
        for key, value in wikis.items():
            if output == False:
                break
            if not value[0].startswith('<img'):
                print('\n\nNot an Image:'+value[0])
            if len(value[1]) < 10:
                print('\n\nShort Text:'+value[0])
            self.assertIn(key, languages)
            self.assertIsInstance(value, tuple)
            self.assertIsInstance(value[0], str)
            self.assertIsInstance(value[1], str)
            self.assertTrue(len(value) == 2)

    if __name__ == "__main__":
        unittest.main()
