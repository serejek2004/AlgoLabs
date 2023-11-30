def get_next_position(needle, automatic_position, char):
    if automatic_position < len(needle) and char == needle[automatic_position]:
        return automatic_position + 1
    else:
        for next_position in range(automatic_position, 0, -1):
            prefix_match = needle[next_position - 1] == char
            suffix_match = needle[:next_position - 1] == needle[(automatic_position - next_position + 1):automatic_position]

            if prefix_match and suffix_match:
                return next_position
        return 0


def calculate_transition_table(needle):

    transition_table = [[0 for _ in needle]
                        for _ in range(len(needle) + 1)]

    for automatic_position in range(len(needle) + 1):
        for index, char in enumerate(needle):
            move_to = get_next_position(needle, automatic_position, char)
            transition_table[automatic_position][index] = move_to

    return transition_table


def search(needle, haystack):

    if not needle:
        return []

    transition_table = calculate_transition_table(needle)

    list_prints = []
    automatic_position = 0
    for index in range(len(haystack)):
        char_ord = (haystack[index])
        if char_ord in needle:
            char_index = needle.index(char_ord)
            automatic_position = transition_table[automatic_position][char_index]
        else:
            automatic_position = 0

        if automatic_position == len(needle):
            list_prints.append(index + 1 - len(needle))

    return list_prints
