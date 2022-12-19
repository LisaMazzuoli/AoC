from first import parse_elves_from_problem_file


def main():
    elves_dict = parse_elves_from_problem_file()
    top_three_tot_calories = 0
    top_three_tot_calories += elves_dict[max(zip(elves_dict.values(), elves_dict.keys()))[1]]
    elves_dict[max(zip(elves_dict.values(), elves_dict.keys()))[1]] = 0
    top_three_tot_calories += elves_dict[max(zip(elves_dict.values(), elves_dict.keys()))[1]]
    elves_dict[max(zip(elves_dict.values(), elves_dict.keys()))[1]] = 0
    top_three_tot_calories += elves_dict[max(zip(elves_dict.values(), elves_dict.keys()))[1]]
    print('la somma delle calorie dei primi tre è ' + str(top_three_tot_calories))


if __name__ == '__main__':
    main()