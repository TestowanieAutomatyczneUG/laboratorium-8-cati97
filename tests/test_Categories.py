import unittest
from src.sample.Categories import *


class TestMealDetails(unittest.TestCase):

    def setUp(self) -> None:
        self.search = Categories()

    def test_get_successful_status_code_200(self):
        self.assertEqual(self.search.get_status_code(), 200)

    def test_check_len_of_categories_correct(self):
        self.assertEqual(self.search.get_len_of_categories(), 14)


if __name__ == '__main__':
    unittest.main()
