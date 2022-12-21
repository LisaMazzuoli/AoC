def read():
    with open("elv6", 'r', encoding='utf-8') as f:
        super_line = [el for line in f for el in line]
    # print(super_line)
    return super_line


def search(super_line, const):
    result = 4  # almeno al quarto posto
    while len(super_line) > 3 and const == 0:
        newset = set(super_line[:4])
        if len(super_line[:4]) == len(newset):
            const = 1
        else:
            result += 1
        super_line.remove(super_line[0])
        newset.clear()

    return result


def main():
    super_line = read()
    const = 0
    result = search(super_line, const)
    if result == len(super_line) and const == 0:
        print('No result')
    else:
        print(f'{result} characters need to be processed')


if __name__ == '__main__':
    main()
