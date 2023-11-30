import unittest
from src.files.finite_automaton import search


class MyTestCase(unittest.TestCase):
    def test_first_case(self):
        self.assertEqual([1, 5], search("ABAA", " ABAAABAA"))

    def test_second_case(self):
        self.assertEqual([1, 12], search("abc", "aabcbaacbacbabc"))

    def test_third_case(self):
        self.assertEqual([0, 4], search("ACBAAC", "ACBAACBAAC"))

    def test_fourth_case(self):
        self.assertEqual(search("", "abcabcc vf abcabcc"), [])

    def test_fifth_case(self):
        self.assertEqual(search("", "abcabcc"), [])

    def test_sixth_case(self):
        self.assertEqual(search("abcabcc", "abc abc abc"), [])

    def test_seventh_case(self):
        self.assertEqual(search("abac", "abacabacabac"), [0, 4, 8])

    def test_eighth_case(self):
        self.assertEqual(search("a", "aaaaaaaaaa       "), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_ninth_case(self):
        self.assertEqual(search("a", "          a,a"), [10, 12])

    def test_tenth_case(self):
        self.assertEqual(search("e", "abcde"), [4])


if __name__ == '__main__':
    unittest.main()
