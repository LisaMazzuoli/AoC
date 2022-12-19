from collections import defaultdict


def parse_elves_from_problem_file():
    elves_dict = defaultdict(int)
    k = 1
    with open("Elves&Calories", 'rt', encoding='utf-8') as f:
        for line in f:
            if line.strip() != '':
                elves_dict['Elv' + str(k)] += int(line)

            else:
                k = k + 1
    return elves_dict


def main():
    elves_dict = parse_elves_from_problem_file()
    # print(d.items())

    elf_with_most_carbs = max(zip(elves_dict.values(), elves_dict.keys()))[1]
    print('Le calorie massime sono di ' + str(elf_with_most_carbs) + ' pari a ' + str(
        elves_dict[elf_with_most_carbs]))


if __name__ == '__main__':
    main()
