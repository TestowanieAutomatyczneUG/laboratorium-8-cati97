import unittest
from src.sample.FindAllStartingWith import *
from assertpy import assert_that


class TestSearchByName(unittest.TestCase):

    def test_get_successful_status_code_200(self):
        self.search = FindAllStartingWith("a")
        self.assertEqual(self.search.get_status_code(), 200)

    def test_first_list_item_starts_wtih_a(self):
        self.search = FindAllStartingWith("a")
        assert_that(self.search.get_list_of_names()[0]).starts_with("A")


if __name__ == '__main__':
    unittest.main()
