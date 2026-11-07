import unittest

from aims.dvd import DigitalVideoDisc
from aims.search import search_by_category


class TestSearch(unittest.TestCase):

    def test_search_by_category(self):
        dvds = [
            DigitalVideoDisc("The Lion King", category="Animation"),
            DigitalVideoDisc("Titanic", category="Romance"),
            DigitalVideoDisc("Frozen", category="Animation")
        ]

        result = search_by_category(dvds, "Animation")

        self.assertEqual(len(result), 2)
        self.assertEqual(
            [dvd.title for dvd in result],
            ["The Lion King", "Frozen"]
        )


if __name__ == "__main__":
    unittest.main()