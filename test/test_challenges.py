import sys
import os
import unittest

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../src")
from challenge_one import string_fun
from challenge_two import append
from challenge_three import list_uniqueness

class TestChallenge(unittest.TestCase):

    def _check_string_fun(self, result, isalpha, endswith_exclam, replace_spaces):
        self.assertEqual(type(result), tuple)
        self.assertEqual(result[0], isalpha)
        self.assertEqual(result[1], endswith_exclam)
        self.assertEqual(result[2], replace_spaces)

    def _check_append(self, l, item, solution):
        append(l, item)
        self.assertEqual(l, solution)

    def _check_list_uniqueness(self, l, length, unique):
        dictionary = list_uniqueness(l)
        self.assertEqual(type(dictionary), dict)
        self.assertEqual(dictionary['list_length'], length)
        self.assertEqual(dictionary['unique_items'], unique)

    def test_challenge_one(self):
        self._check_string_fun(string_fun('Hello World!'), False, True, 'Hello-World!')
        self._check_string_fun(string_fun('ThisIsAChallenge'), True, False, 'ThisIsAChallenge')
        self._check_string_fun(string_fun('    '), False, False, '----')

    def test_challenge_two(self):
        self._check_append([1, 2, 3], 4, [1, 2, 3, 4])
        self._check_append(['a','b', 'c'], 'd', ['a','b','c','d'])

    def test_challenge_three(self):
        self._check_list_uniqueness([1, 2, 2, 4], 4, 3)
        self._check_list_uniqueness(['a', 'a', 'a', 1], 4, 2)


if __name__ == '__main__':
    unittest.main()