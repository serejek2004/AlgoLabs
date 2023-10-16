import unittest

from files.ilona_task import ilona_tester


class TestsIlona(unittest.TestCase):
    def test_if_number_is_not_exist(self):
        array_numbers = [1, 2, 3]
        selected_number = 5
        self.assertEqual(ilona_tester(array_numbers, selected_number), False)

    def test_min_limit_elements(self):
        array_numbers = [1, 2]
        selected_number = 5
        self.assertEqual(ilona_tester(array_numbers, selected_number), False)

    def test_min_value_number(self):
        array_numbers = [1, 2, 3, 0]
        selected_number = 5
        self.assertEqual(ilona_tester(array_numbers, selected_number), False)

    def test_max_limit_elements(self):
        array_numbers = []
        for i in range(1001):
            array_numbers.append(i)
        selected_number = 6
        self.assertEqual(ilona_tester(array_numbers, selected_number), False)

    def test_max_value_number(self):
        array_numbers = [1, 2, 3, 4, 2e10]
        selected_number = 6
        self.assertEqual(ilona_tester(array_numbers, selected_number), False)

    def test_min_selected_number_value(self):
        array_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        selected_number = 0
        self.assertEqual(ilona_tester(array_numbers, selected_number), False)

    def test_max_selected_number_value(self):
        array_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        selected_number = 2e10
        self.assertEqual(ilona_tester(array_numbers, selected_number), False)

    def test_no_exist_number(self):
        array_numbers = [1, 3, 5, 5, 5, 5, 5, 5, 5]
        selected_number = 11
        self.assertEqual(ilona_tester(array_numbers, selected_number), False)

    def test_if_number_is_exist_with_duplicates(self):
        array_numbers = [1, 3, 5, 5, 5, 5, 7, 8, 4, 5, 5, 5, 5]
        selected_number = 11
        self.assertEqual(ilona_tester(array_numbers, selected_number), True)

    def test_good_variant(self):
        array_numbers = [1, 2, 3, 4]
        selected_number = 6
        self.assertEqual(ilona_tester(array_numbers, selected_number), True)


if __name__ == '__main__':
    unittest.main()
