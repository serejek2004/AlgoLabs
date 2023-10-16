def calculate_seeds(array):
    result = []

    for row in range(array.__len__()):
        if row % 2 == 0:
            for column in range(array[row].__len__()):
                result.append(array[row][column])
        else:
            for column in range(array[row].__len__() - 1, -1, -1):
                result.append(array[row][column])

    return result
