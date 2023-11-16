import unittest
from program.penguins import find_unavailable_city_for_gas_container


class MyTestCase(unittest.TestCase):
    def test_first_case(self):
        cities_list = ['Львів', 'Стрий', 'Долина']
        gas_containers_list = ['Газосховище_1', 'Газосховище_2']
        active_connections_list = [['Львів', 'Стрий'], ['Стрий', 'Долина'], ['Газосховище_1', 'Газосховище_2'],
                                   ['Газосховище_1', 'Львів']]
        result = find_unavailable_city_for_gas_container(cities_list, gas_containers_list, active_connections_list)
        self.assertEqual(str(result), "[['Газосховище_2', ['Львів', 'Стрий', 'Долина']]]")

    def test_second_case(self):
        cities_list = ['Львів', 'Стрий', 'Долина',]
        gas_containers_list = ['Газосховище_1', 'Газосховище_2', 'Газосховище_3']
        active_connections_list = [['Львів', 'Стрий'], ['Стрий', 'Долина'], ['Газосховище_1', 'Газосховище_2'],
                                   ['Газосховище_1', 'Львів']]
        result = find_unavailable_city_for_gas_container(cities_list, gas_containers_list, active_connections_list)
        self.assertEqual(str(result), "[['Газосховище_2', ['Львів', 'Стрий', 'Долина']], "
                                      "['Газосховище_3', ['Львів', 'Стрий', 'Долина']]]")

    def test_third_case(self):
        cities_list = ['Львів', 'Стрий', 'Долина',]
        gas_containers_list = ['Газосховище_1', 'Газосховище_2', 'Газосховище_3']
        active_connections_list = [['Львів', 'Стрий'], ['Стрий', 'Долина'], ['Газосховище_2', 'Газосховище_1'],
                                   ['Газосховище_1', 'Львів']]
        result = find_unavailable_city_for_gas_container(cities_list, gas_containers_list, active_connections_list)
        self.assertEqual(str(result), "[['Газосховище_3', ['Львів', 'Стрий', 'Долина']]]")

    def test_fourth_case(self):
        cities_list = ['Львів', 'Стрий', 'Долина',]
        gas_containers_list = ['Газосховище_1', 'Газосховище_2', 'Газосховище_3']
        active_connections_list = [['Львів', 'Стрий'], ['Стрий', 'Долина'], ['Газосховище_2', 'Газосховище_1'],
                                   ['Газосховище_1', 'Львів'], ['Газосховище_3', 'Газосховище_2']]
        result = find_unavailable_city_for_gas_container(cities_list, gas_containers_list, active_connections_list)
        self.assertEqual(str(result), "[]")

    def test_fifth_case(self):
        cities_list = ['Львів', 'Стрий', 'Долина', ]
        gas_containers_list = ['Газосховище_1', 'Газосховище_2', 'Газосховище_3']
        active_connections_list = [['Львів', 'Стрий'], ['Долина', 'Львів']]
        result = find_unavailable_city_for_gas_container(cities_list, gas_containers_list, active_connections_list)

        self.assertEqual(str(result), "[['Газосховище_1', ['Львів', 'Стрий', 'Долина']], "
                                      "['Газосховище_2', ['Львів', 'Стрий', 'Долина']], "
                                      "['Газосховище_3', ['Львів', 'Стрий', 'Долина']]]")


if __name__ == '__main__':
    unittest.main()
