import unittest
from password import Password


class TestCardNum(unittest.TestCase):  # test class
    def setUp(self):
        self.password = Password()

    def test_valid_num(self):
        self.assertEqual(self.password.password_validation("456GHJIijhbvn+"), True)

    def test_invalid_num(self):
        self.assertEqual(self.password.password_validation("456GHJIijhbvn"), False)

    def test_non_num_input(self):
        self.assertEqual(self.password.password_validation("GHJIijhbvn+"), False)

    def test_non_letter_input(self):
        self.assertEqual(self.password.password_validation("456+"), False)