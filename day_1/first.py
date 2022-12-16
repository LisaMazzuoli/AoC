def function(dict):
    k = 1
    count = 0
    with open("Elves&Calories", 'rt', encoding='utf-8') as f:
        for line in f:
            if count == 0:
                dict['Elv' + str(k)] = 0
            if line.strip() != '':
                dict['Elv' + str(k)] += int(line)
                count = 1

            else:
                k = k + 1
                count = 0
    return dict


def main():
    d = {}
    d = function(d)
    # print(d.items())
    print('Le calorie massime sono di ' + str(max(zip(d.values(), d.keys()))[1]) + ' pari a ' + str(
        d[max(zip(d.values(), d.keys()))[1]]))


if __name__ == '__main__':
    main()