def get_next_position(needle, automatic_position, char):
    if automatic_position < len(needle) and char == needle[automatic_position]:
        return automatic_position + 1
    elif automatic_position > 0 and char == needle[0]:
        return 1
    else:
        return 0


def calculate_transition_table(needle):

    transition_table = [[0 for _ in needle]
                        for _ in range(len(needle) + 1)]

    for automatic_position in range(len(needle) + 1):
        for index, char in enumerate(needle):
            transition_table[automatic_position][index] = get_next_position(needle, automatic_position, char)

    return transition_table


def search(needle, haystack):

    if not needle:
        return []

    transition_table = calculate_transition_table(needle)

    list_prints = []
    automatic_position = 0
    for index in range(len(haystack)):
        char = (haystack[index])
        if char in needle:
            char_index = needle.index(char)
            automatic_position = transition_table[automatic_position][char_index]
        else:
            automatic_position = 0

        if automatic_position == len(needle):
            list_prints.append(index + 1 - len(needle))

    return list_prints
