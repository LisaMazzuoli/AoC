from first import read_and_rewrite
from first import exact_positions


def reordering(moves, final_dict):
    for skip in moves:
        number_of_moves = skip[0]
        from_where = skip[1]
        to_where = skip[2]
        #while number_of_moves > 0:
        crate_to_move = final_dict[from_where][-number_of_moves:]
        del final_dict[from_where][-number_of_moves:]
        if isinstance(final_dict[to_where], list):  # è di tipo lista
            final_dict[to_where].extend(crate_to_move)
            #final_dict[to_where] + crate_to_move
        else: # è una stringa
            final_dict[to_where] = list(final_dict[to_where]).extend(crate_to_move)
        #    number_of_moves -= 1
        crate_to_move.clear()
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
