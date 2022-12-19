def parse_elves_from_problem_file():
    elves_dict = dict()
    k = 1
    count = 0
    with open("Elves&Calories", 'rt', encoding='utf-8') as f:
        for line in f:
            if count == 0:
                elves_dict['Elv' + str(k)] = 0
            if line.strip() != '':
                elves_dict['Elv' + str(k)] += int(line)
                count = 1

            else:
                k = k + 1
                count = 0
    return elves_dict


def main():
    elves_dict = parse_elves_from_problem_file()
    # print(d.items())
    print('Le calorie massime sono di ' + str(max(zip(elves_dict.values(), elves_dict.keys()))[1]) + ' pari a ' + str(
        elves_dict[max(zip(elves_dict.values(), elves_dict.keys()))[1]]))


if __name__ == '__main__':
    main()
