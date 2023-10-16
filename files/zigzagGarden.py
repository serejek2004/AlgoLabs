def calculate_array(zigzag_array):

    result = []

    if not zigzag_array:
        return result

    m, n = len(zigzag_array), len(zigzag_array[0])

    for level in range(m + n - 1):
        if level % 2 == 0:
            if level < m:
                for i in range(max(0, level - n + 1), min(level + 1, m)):
                    result.append(zigzag_array[i][level - i])
            else:
                for i in range(max(0, level - n + 1), m):
                    result.append(zigzag_array[i][level - i])
        else:
            if level < n:
                for i in range(max(0, level - m + 1), min(level + 1, n)):
                    result.append(zigzag_array[level - i][i])
            else:
                for i in range(max(0, level - m + 1), n):
                    result.append(zigzag_array[level - i][i])

    return result
