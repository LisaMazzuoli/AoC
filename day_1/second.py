from first import parse_elves_from_problem_file


def main():
    d = parse_elves_from_problem_file()
    sum = 0
    sum += d[max(zip(d.values(), d.keys()))[1]]
    d[max(zip(d.values(), d.keys()))[1]] = 0
    sum += d[max(zip(d.values(), d.keys()))[1]]
    d[max(zip(d.values(), d.keys()))[1]] = 0
    sum += d[max(zip(d.values(), d.keys()))[1]]
    print('la somma delle calorie dei primi tre è ' + str(sum))


if __name__ == '__main__':
    main()