from first_bis import read


def intersection(first_list, second_list):
    aux_list = [value for value in first_list if value in second_list]
    if len(aux_list) != 0:
        return 1
    else:
        return 0


def count_overlaps(list_of_positions):
    overlaps = 0
    for line in list_of_positions:
        first_range = [i for i in range(line[0], line[1] + 1)]
        second_range = [i for i in range(line[2], line[3] + 1)]
        overlaps += intersection(first_range, second_range)
    return overlaps


def main():
    list_of_positions = read()
    num_ranges_overlap = count_overlaps(list_of_positions)
    print(f'il numero di sovrapposizioni è {num_ranges_overlap}')


if __name__ == '__main__':
    main()
