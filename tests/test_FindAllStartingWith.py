import unittest
from src.sample.FindAllStartingWith import *


class TestSearchByName(unittest.TestCase):

    def test_get_successful_status_code_200(self):
        self.search = FindAllStartingWith("a")
        self.assertEqual(self.search.get_status_code(), 200)

if __name__ == '__main__':
    unittest.main()
