import unittest

from files.snakeGarden import calculate_seeds


class TestRobot(unittest.TestCase):
    def test_first_case(self):
        array = [[1, 2, 3, 4, 5],
                 [6, 7, 8, 9, 10],
                 [11, 12, 13, 14, 15],
                 [16, 17, 18, 19, 20],
                 [21, 22, 23, 24, 25]]
        self.assertEqual(calculate_seeds(array),
                         [1, 2, 3, 4, 5, 10, 9, 8, 7, 6, 11, 12, 13, 14, 15, 20, 19, 18, 17, 16, 21, 22, 23, 24, 25])

    def test_second_case(self):
        array = [[2, 5, 7, 8], [17, 2, 19, 4]]
        self.assertEqual(calculate_seeds(array), [2, 5, 7, 8, 4, 19, 2, 17])

    def test_third_case(self):
        array = [[1, 2, 3, 4, 5, 6]]
        self.assertEqual(calculate_seeds(array), [1, 2, 3, 4, 5, 6])


if __name__ == '__main__':
    unittest.main()
