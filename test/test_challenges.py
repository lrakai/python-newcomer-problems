import sys
import os
import unittest

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../src")
from challenge_one import string_fun

class TestChallenge(unittest.TestCase):

    def _check_string_fun(self, result, isalpha, endswith_exclam, replace_spaces):
        self.assertEqual(type(result), tuple)
        self.assertEqual(result[0], isalpha)
        self.assertEqual(result[1], endswith_exclam)
        self.assertEqual(result[2], replace_spaces)


    def test_challenge_one(self):
        self._check_string_fun(string_fun('Hello World!'), False, True, 'Hello-World!')
        self._check_string_fun(string_fun('ThisIsAChallenge'), True, False, 'ThisIsAChallenge')
        self._check_string_fun(string_fun('    '), False, False, '----')

    def test_challenge_two(self):
        pass

    def test_challenge_three(self):
        pass


if __name__ == '__main__':
    unittest.main()