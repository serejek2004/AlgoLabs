def flood_fill(matrix_to_change, coordinate_x, coordinate_y, letter_to_change):
    rows = len(matrix_to_change)
    columns = len(matrix_to_change[0])
    united_coordinate = matrix_to_change[coordinate_x - 1][coordinate_y - 1]

    def fill_position(x, y):
        if x < 0 or x >= rows:
            return
        if y < 0 or y >= columns:
            return
        if matrix_to_change[x][y] != united_coordinate:
            return

        matrix_to_change[x][y] = letter_to_change

        fill_position(x - 1, y)
        fill_position(x, y - 1)
        fill_position(x + 1, y)
        fill_position(x, y + 1)

    fill_position(coordinate_x - 1, coordinate_y - 1)


def read_from_file(file_name):
    with open(file_name, 'r') as file_name:
        coordinate = file_name.readline()
        coordinate = coordinate.split(',')
        x = int(coordinate[0])
        y = int(coordinate[1])
        new_letter = file_name.readline().strip()
        read_matrix = []

        for row in file_name:
            row = row.strip().split(',')
            cleaned_row = []
            for cell in row:
                cleaned_cell = cell.strip(" '[]")
                if cleaned_cell:
                    cleaned_row.append(cleaned_cell)
            read_matrix.append(cleaned_row)

    return read_matrix, x, y, new_letter


def write_to_file(file_name, matrix_after_flood_fill):
    with open(file_name, 'w') as file:
        for row in matrix_after_flood_fill:
            line = ', '.join(row)
            file.write(line + '\n')


matrix, x_coordinate, y_coordinate, letter = read_from_file("input.txt")
flood_fill(matrix, x_coordinate, y_coordinate, letter)
write_to_file("output.txt", matrix)
