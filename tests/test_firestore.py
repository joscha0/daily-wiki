import unittest
from db import firestore


class TestFirestore(unittest.TestCase):

    def test_adduser(self):
        result = firestore.adduser("joschavonandrian@gmail.com", "en")
        self.assertFalse(result)

    if __name__ == "__main__":
        unittest.main()
