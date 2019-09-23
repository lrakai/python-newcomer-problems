import sys
import os
import unittest

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../src")
from challenge_one import string_fun
from challenge_two import append

class TestChallenge(unittest.TestCase):

    def _check_string_fun(self, result, isalpha, endswith_exclam, replace_spaces):
        self.assertEqual(type(result), tuple)
        self.assertEqual(result[0], isalpha)
        self.assertEqual(result[1], endswith_exclam)
        self.assertEqual(result[2], replace_spaces)

    def _check_append(self, l, item, solution):
        append(l, item)
        self.assertEqual(l, solution)

    def test_challenge_one(self):
        self._check_string_fun(string_fun('Hello World!'), False, True, 'Hello-World!')
        self._check_string_fun(string_fun('ThisIsAChallenge'), True, False, 'ThisIsAChallenge')
        self._check_string_fun(string_fun('    '), False, False, '----')

    def test_challenge_two(self):
        self._check_append([1, 2, 3], 4, [1, 2, 3, 4])
        self._check_append(['a','b', 'c'], 'd', ['a','b','c','d'])

    def test_challenge_three(self):
        pass


if __name__ == '__main__':
    unittest.main()