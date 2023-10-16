import unittest

from files.zigzagGarden import calculate_array


class TestRobot(unittest.TestCase):
    def test_first_case(self):
        array = [[1, 2, 3, 4, 5],
                 [6, 7, 8, 9, 10],
                 [11, 12, 13, 14, 15],
                 [16, 17, 18, 19, 20],
                 [21, 22, 23, 24, 25]]
        from files.zigzagGarden import calculate_array
        self.assertEqual(calculate_array(array),
                         [1, 6, 2, 3, 7, 11, 16, 12, 8, 4, 5, 9, 13, 17, 21, 22, 18, 14, 10, 15, 19, 23, 24, 20, 25])

    def test_second_case(self):
        array = [[2, 5, 7, 8], [17, 2, 19, 4]]
        self.assertEqual(calculate_array(array), [2, 17, 5, 7, 2, 19, 8, 4])

    def test_third_case(self):
        array = [[1, 2, 3, 4, 5, 6]]
        self.assertEqual(calculate_array(array), [1, 2, 3, 4, 5, 6])

    def test_fourth_case(self):
        array = [[1], [2], [3], [4], [5], [6]]
        self.assertEqual(calculate_array(array), [1, 2, 3, 4, 5, 6])


if __name__ == '__main__':
    unittest.main()
