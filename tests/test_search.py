import unittest

from aims.dvd import DigitalVideoDisc
from aims.search import search_by_title


class TestSearch(unittest.TestCase):

    def test_search_by_title_case_insensitive(self):
        dvds = [
            DigitalVideoDisc("The Lion King"),
            DigitalVideoDisc("Titanic")
        ]

        result = search_by_title(dvds, "lion")

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].title, "The Lion King")


if __name__ == "__main__":
    unittest.main()