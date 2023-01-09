"""No modules"""


def read():
    """I read and save the fie as matrix"""
    tabs_of_height = []
    with open("elv8", 'r', encoding='utf-8') as file:
        for line in file:
            tabs_of_height.append([int(num) for num in list(line.replace("\n", ""))])
    return tabs_of_height


def count_lines():
    """Counts the number of lines"""
    num_of_lines = 0
    with open("elv8", 'r', encoding='utf-8') as file:
        # num_of_lines = len(file.readline())
        for _ in file:
            num_of_lines += 1
    return num_of_lines


def check_for_visibility(tabs_of_height, line, column, num_of_lines, num_of_columns):
    """Count the visibility of each tree"""
    count = 0
    product = 1
    control = 1
    if line != 0:
        for element in range(line - 1, -1, -1):
            if tabs_of_height[element][column] < tabs_of_height[line][column]:
                if control == 1:
                    count += 1
            else:
                if control == 1:
                    control = 0
                    count += 1
        product *= count
        count = 0
        control = 1

    if line != (num_of_lines - 1):
        for element in range(line + 1, num_of_lines):
            if tabs_of_height[element][column] < tabs_of_height[line][column]:
                if control == 1:
                    count += 1
            else:
                if control == 1:
                    control = 0
                    count += 1
        product *= count
        count = 0
        control = 1

    if column != 0:
        for element in range(column - 1, -1, -1):
            if tabs_of_height[line][element] < tabs_of_height[line][column]:
                if control == 1:
                    count += 1
            else:
                if control == 1:
                    control = 0
                    count += 1
        product *= count
        count = 0
        control = 1

    if column != (num_of_columns - 1):
        for element in range(column + 1, num_of_columns):
            if tabs_of_height[line][element] < tabs_of_height[line][column]:
                if control == 1:
                    count += 1
            else:
                if control == 1:
                    control = 0
                    count += 1
        product *= count
    return product


def highest_scenic_score(tabs_of_height, num_of_lines, num_of_columns):
    """Find the tree with the highest view"""
    count_of_trees = 0
    for line in range(num_of_lines - 1):
        for column in range(num_of_columns - 1):
            count_of_trees = max(count_of_trees,
                                 check_for_visibility(tabs_of_height, line, column, num_of_lines, num_of_columns))
    return count_of_trees


def main():
    """main"""
    num_of_lines = count_lines()
    tabs_of_height = read()
    num_of_columns = len(tabs_of_height[0])
    visible_trees = highest_scenic_score(tabs_of_height, num_of_lines, num_of_columns)
    print(f'The highest scenic score is {visible_trees}')


if __name__ == '__main__':
    main()
