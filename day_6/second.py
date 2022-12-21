from first import read


def search(super_line, const):
    result = 14  # almeno al quarto posto
    while len(super_line) > 13 and const == 0:
        newset = set(super_line[:14])
        if len(super_line[:14]) == len(newset):
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
