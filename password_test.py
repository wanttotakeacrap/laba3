import unittest
from password import Password


class TestCardNum(unittest.TestCase):  # test class
    def setUp(self):
        self.password = Password()

    def test_valid_num(self):
        result = str(self.password.data_from_file('test_data/test_input.txt')).strip()
        self.assertIn('456GHJIijhbvn+', result)

    def test_invalid_num(self):
        result = self.password.data_from_file('test_data/test_input.txt')
        self.assertNotIn('invalid_number', result)

    def test_empty_file(self):
        result = self.password.data_from_file('test_data/empty_file.txt')
        self.assertEqual(result, [])

    def test_non_num_input(self):
        result = self.password.data_from_file('test_data/non_numeric_input.txt')
        self.assertEqual(result, [])

    def test_non_letter_input(self):
        result = self.password.data_from_file('test_data/non_letter_input.txt')
        self.assertEqual(result, [])