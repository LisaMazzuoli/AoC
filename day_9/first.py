"""None"""


def read():
    """Reading file"""
    new_reading = []
    with open("elv9", "r", encoding="utf-8") as file:
        reading = [line.replace("\n", "") for line in file]
    for line in reading:
        new_reading.append([command for command in line.split(" ")])
    return new_reading


def zero_matrix_maker(n):
    """Gives an empty matrix"""
    matrix_of_zeros = []
    for _ in range(n):
        matrix_of_zeros.append([['E', 'E', 0] for _ in range(n)])
    return matrix_of_zeros


def search_for_t(line, column, positions_matrix):
    count = 0
    if (positions_matrix[line][max(column - 1, 0)][1] == 'T') or (
            positions_matrix[line][min(column + 1, 699)][1] == 'T'):
        count = 1
    elif (positions_matrix[max(line - 1, 0)][column][1] == 'T') or (
            positions_matrix[min(line + 1, 699)][column][1] == 'T'):
        count = 1
    elif (positions_matrix[min(line + 1, 699)][min(column + 1, 699)][1] == 'T') or (
            positions_matrix[max(line - 1, 0)][min(column + 1, 699)][1] == 'T'):
        count = 1
    elif (positions_matrix[min(line + 1, 699)][max(column - 1, 0)][1] == 'T') or (
            positions_matrix[max(line - 1, 0)][max(column - 1, 0)][1] == 'T'):
        count = 1
    elif positions_matrix[line][column][1] == 'T':
        count = 1
    return count


def walks(positions_matrix, moves):
    last_line = 300
    last_column = 150
    positions_matrix[300][150] = ['H', 'T', 1]
    previous_position = [300, 150]  # ultima posizione di T
    while len(moves) > 0:
        if moves[0][0] == 'R':
            for column in range(last_column + 1, last_column + int(moves[0][1]) + 1, 1):
                positions_matrix[last_line][column][0] = 'H'
                check = search_for_t(last_line, column, positions_matrix)
                if check == 0:  # significa che non sta intorno e devo spostare
                    positions_matrix[last_line][column - 1][1] = 'T'
                    positions_matrix[previous_position[0]][previous_position[1]][1] = 'E'
                    previous_position = [last_line, column - 1]
                    positions_matrix[last_line][column - 1][2] = 1
            last_column += int(moves[0][1])
        elif moves[0][0] == "L":
            for column in range(last_column - 1, last_column - int(moves[0][1]) - 1, -1):
                positions_matrix[last_line][column][0] = 'H'
                check = search_for_t(last_line, column, positions_matrix)
                if check == 0:
                    positions_matrix[last_line][column + 1][1] = 'T'
                    positions_matrix[previous_position[0]][previous_position[1]][1] = 'E'
                    previous_position = [last_line, column + 1]
                    positions_matrix[last_line][column + 1][2] = 1
            last_column -= int(moves[0][1])
        elif moves[0][0] == 'U':
            for line in range(last_line - 1, last_line - int(moves[0][1]) - 1, -1):
                positions_matrix[line][last_column][0] = 'H'
                check = search_for_t(line, last_column, positions_matrix)
                if check == 0:
                    positions_matrix[line + 1][last_column][1] = 'T'
                    positions_matrix[previous_position[0]][previous_position[1]][1] = 'E'
                    previous_position = [line + 1, last_column]
                    positions_matrix[line + 1][last_column][2] = 1
            last_line -= int(moves[0][1])
        else:
            for line in range(last_line + 1, last_line + int(moves[0][1]) + 1, 1):
                positions_matrix[line][last_column][0] = 'H'
                check = search_for_t(line, last_column, positions_matrix)
                if check == 0:
                    positions_matrix[line - 1][last_column][1] = 'T'
                    positions_matrix[previous_position[0]][previous_position[1]][1] = 'E'
                    previous_position = [line - 1, last_column]
                    positions_matrix[line - 1][last_column][2] = 1
            last_line += int(moves[0][1])
        del moves[0]
    positions_visited = 0
    for line in positions_matrix:
        for element in line:
            positions_visited += element[2]

    return positions_visited


def main():
    """main"""
    positions_matrix = zero_matrix_maker(700)  # come ottimizzare?
    moves = read()
    positions_visited = walks(positions_matrix, moves)
    print(f'Le posizioni visitate almeno una volta sono {positions_visited}')


if __name__ == '__main__':
    main()
