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
    sum = 0
    sum += d[max(zip(d.values(), d.keys()))[1]]
    d[max(zip(d.values(), d.keys()))[1]] = 0
    sum += d[max(zip(d.values(), d.keys()))[1]]
    d[max(zip(d.values(), d.keys()))[1]] = 0
    sum += d[max(zip(d.values(), d.keys()))[1]]
    print('la somma delle calorie dei primi tre è ' + str(sum))


if __name__ == '__main__':
    main()