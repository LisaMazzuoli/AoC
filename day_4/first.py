def read():
    lista = []
    with open("elv4", 'rt', encoding='utf-8') as f:
        for line in f:
            lista.append(line.replace("\n", ""))
        list1 = [int(door_number) for line in lista for half in line.split(',') for door_number in half.split('-')]
    return list1


def pairs_in_others(list_of_positions):
    result = 0
    while len(list_of_positions) > 0:
        if list_of_positions[0] >= list_of_positions[2] and list_of_positions[1] <= list_of_positions[3]:
            result += 1
        elif list_of_positions[0] <= list_of_positions[2] and list_of_positions[1] >= list_of_positions[3]:
            result += 1
        del list_of_positions[:4]
    return result


def main():
    list_of_positions = read()
    tot_pairs_in_others = pairs_in_others(list_of_positions)
    print(f'La somma delle inclusioni è {tot_pairs_in_others}')


if __name__ == '__main__':
    main()
