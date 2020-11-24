import unittest
from src.sample.MealDetailsById import *


class TestMealDetails(unittest.TestCase):

    def test_get_successful_status_code_200(self):
        self.search = MealDetailsById(52772)
        self.assertEqual(self.search.get_status_code(), 200)

    def test_check_correct_id(self):
        self.search = MealDetailsById(52772)
        self.assertEqual(self.search.check_if_correct_meal(), True)

    def test_check_correct_id_false(self):
        self.search = MealDetailsById(251)
        self.assertEqual(self.search.get_status_code(), 200)


if __name__ == '__main__':
    unittest.main()
