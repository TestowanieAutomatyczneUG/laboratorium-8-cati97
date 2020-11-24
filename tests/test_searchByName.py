import unittest
from src.sample.SearchByName import *


class TestSearchByName(unittest.TestCase):

    def test_get_successful_status_code_200(self):
        self.search = SearchByName("Arrabiata")
        self.assertEqual(self.search.get_status_code(), 200)

    def test_get_correct_meal(self):
        self.search = SearchByName("Arrabiata")
        self.assertEqual(self.search.check_if_correct_meal(), True)

    def test_get_incorrect_meal(self):
        self.search = SearchByName("Sa")
        self.assertEqual(self.search.check_if_correct_meal(), False)


if __name__ == '__main__':
    unittest.main()
