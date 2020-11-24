# the inclusion of the tests module is not meant to offer best practices for
# testing in general, but rather to support the `find_packages` example in
# setup.py that excludes installing the "tests" package

import unittest
from src.sample.SearchByName import *


class TestSearchByName(unittest.TestCase):

    def test_get_successful_status_code_200(self):
        self.search = SearchByName("Arrabiata")
        self.assertEqual(self.search.get_status_code(), 200)


if __name__ == '__main__':
    unittest.main()
