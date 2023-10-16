import numpy as np


def ilona_tester(list_numbers, summary_number):
    if summary_number < 6:
        return False

    if summary_number <= 1 or 3 * 10 ** 9 <= summary_number:
        print("Conditions are violated")
        return False

    if 1000 <= list_numbers.__len__() or list_numbers.__len__() <= 3:
        print("Conditions are violated")
        return False

    list_numbers.sort()
    list_numbers = np.unique(list_numbers)

    for i in list_numbers:
        if 1 > i or i > 3 * 10 ** 9:
            print("Conditions are violated")
            return False

    # left = 0
    # right = list_numbers.__len__() - 1
    # middle = right // 2
    #
    # while left < right:
    #
    #     if summary_number <= list_numbers[left] + list_numbers[right]:
    #         right -= 1
    #
    #     if summary_number > list_numbers[left] + list_numbers[right] + list_numbers[middle]:
    #         middle = middle // 2
    #
    #     elif summary_number == list_numbers[left] + list_numbers[right] + list_numbers[middle]:
    #         return True
    #
    #     else:
    #         middle = (right - middle) // 2

    start = 1
    end = len(list_numbers) - 1
    mid = 0
    while start < end:
        mid = summary_number - (list_numbers[start] + list_numbers[end])
        if summary_number < (list_numbers[start] + list_numbers[end] + list_numbers[mid]):
            end -= 1
        else:
            start = mid + 1

        if summary_number == (list_numbers[start] + list_numbers[end] + mid):

            return True

        else:
            return False


    print("such numbers do not exist")
    return False
