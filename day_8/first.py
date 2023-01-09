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
        for _ in file:
            num_of_lines += 1
    return num_of_lines


def trees_around_the_edge(tabs_of_height, num_of_lines):
    """Counts the number of trees around the edge"""
    num_of_columns = len(tabs_of_height[0])
    count_of_trees = 0
    for column in range(num_of_columns):
        if tabs_of_height[0][column]:
            count_of_trees += 1
        if tabs_of_height[num_of_lines - 1][column]:
            count_of_trees += 1
    for line in range(1, num_of_lines - 1):
        if tabs_of_height[line][0]:
            count_of_trees += 1
        if tabs_of_height[line][num_of_columns - 1]:
            count_of_trees += 1
    return count_of_trees


def check_for_visibility(tabs_of_height, line, column, num_of_lines, num_of_columns):
    """Check the visibility of each tree"""
    count = 0
    for element in range(line):
        if tabs_of_height[element][column] >= tabs_of_height[line][column]:
            count += 1
    if count == 0:
        return 1
    count = 0
    for element in range(line + 1, num_of_lines):
        if tabs_of_height[element][column] >= tabs_of_height[line][column]:
            count += 1
    if count == 0:
        return 1
    count = 0
    for element in range(column):
        if tabs_of_height[line][element] >= tabs_of_height[line][column]:
            count += 1
    if count == 0:
        return 1
    count = 0
    for element in range(column + 1, num_of_columns):
        if tabs_of_height[line][element] >= tabs_of_height[line][column]:
            count += 1
    if count == 0:
        return 1
    count = 0
    return count


def interior_visible_trees(tabs_of_height, num_of_lines, num_of_columns):
    """Count how many interior trees are visible from outside"""
    count_of_trees = 0
    for line in range(1, num_of_lines - 1):
        for column in range(1, num_of_columns - 1):
            count_of_trees += check_for_visibility(tabs_of_height, line, column, num_of_lines, num_of_columns)
    return count_of_trees


def main():
    """main"""
    num_of_lines = count_lines()
    tabs_of_height = read()
    num_of_columns = len(tabs_of_height[0])
    visible_trees = (num_of_columns - 2) * 4 + 4
    visible_trees += interior_visible_trees(tabs_of_height, num_of_lines, num_of_columns)
    print(f'The trees visible from outside the grid are {visible_trees}')


if __name__ == '__main__':
    main()
