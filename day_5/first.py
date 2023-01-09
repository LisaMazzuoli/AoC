def read_and_rewrite():
    with open("elv5") as f:
        contents1, sentinel, contents2 = f.read().partition('-')  # ho dovuto aggiungere '-' alla riga, come
    with open("tabella_pile", "w") as f:  # cercare la riga vuota?
        f.write(contents1)
    with open("spostamenti", "w") as f:
        f.write(contents2)
    moves = []
    with open("spostamenti", 'r', encoding='utf-8') as f:
        for line in f:
            moves.append([int(el) for el in line.split() if el.isdigit()])
    moves.remove([])
    return moves


def exact_positions():
    position_dict = {}
    with open("tabella_pile", 'r', encoding='utf-8') as f:
        last_line = f.readlines()[-1]
    with open("tabella_pile", 'r', encoding='utf-8') as f:
        for line in f:
            my_position = 0  # mi fa sapere in che posizione della lista sto anche se ci sono ripetizioni
            for el in line:
                if el.isupper():  # controllo se è una lettera maiuscola
                    if int(last_line[my_position]) not in position_dict:
                        position_dict[int(last_line[my_position])] = el
                    elif isinstance(position_dict[int(last_line[my_position])], list):
                        position_dict[int(last_line[my_position])].append(el)
                    else:
                        position_dict[int(last_line[my_position])] = [position_dict[int(last_line[my_position])], el]
                my_position += 1
    for keys in position_dict:
        if len(position_dict[keys]) > 1:
            position_dict[keys].reverse()
    return position_dict


def reordering(moves, final_dict):
    for skip in moves:
        number_of_moves = skip[0]
        while number_of_moves > 0:
            change = final_dict[skip[1]].pop(-1)
            if isinstance(final_dict[skip[2]], list):  # è di tipo lista
                final_dict[skip[2]].append(change)
            else:
                final_dict[skip[2]] = [final_dict[skip[2]], change]
            number_of_moves -= 1
    result = ''
    list_of_keys = [keys for keys in final_dict]
    for key in sorted(list_of_keys):
        result += final_dict[key].pop(-1)
    return result


def main():
    moves = read_and_rewrite()
    position_dict = exact_positions()
    final_crate = reordering(moves, position_dict)
    print(f'final_crate={final_crate}')


if __name__ == '__main__':
    main()
