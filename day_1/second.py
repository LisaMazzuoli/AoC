from first import parse_elves_from_problem_file


def main():
    elves_dict = parse_elves_from_problem_file()
    top_n_tot_calories = 0
    top_calories_number = 3
    for _ in range(top_calories_number):
        top_scoring_elf = max(elves_dict, key=elves_dict.get)
        top_n_tot_calories += elves_dict[top_scoring_elf]
        del elves_dict[top_scoring_elf]

    print('la somma delle calorie dei primi tre è ' + str(top_n_tot_calories))


if __name__ == '__main__':
    main()