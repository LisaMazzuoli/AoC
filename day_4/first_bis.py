def read():
    lista = []
    with open("elv4", 'rt', encoding='utf-8') as f:
        for line in f:
            # lista.append(line.replace("\n", ""))
            lista.append([int(door_number) for half in line.split(',') for door_number in half.split('-')])
    return lista


def pairs_in_others(list_of_positions):
    result = 0
    for line in list_of_positions:
        if line[0] >= line[2] and line[1] <= line[3]:
            result += 1
        elif line[0] <= line[2] and line[1] >= line[3]:
            result += 1
    return result


def main():
    list_of_positions = read()
    tot_pairs_in_others = pairs_in_others(list_of_positions)
    print(f'La somma delle inclusioni è {tot_pairs_in_others}')


if __name__ == '__main__':
    main()
