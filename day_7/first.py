# from ..day_6.first import read

def read():
    with open("prova", 'r', encoding='utf-8') as f:
        read_file = [line.replace("\n", "") for line in f]
    return read_file


def content_reading(root, my_commands, count):
    # modifica la lista my_commands
    while "$" not in my_commands[0]:
        root.append([half[-1] for half in my_commands[0].split(' ')])
    for el in root:
        if el.isdigit:
            el = int(el)

    return


def main():
    my_commands = read()
    root = []
    count = 0
    while len(my_commands) != 0:
        if "$" in my_commands[0]:
            if "cd" in my_commands[0]:
                lowercase = [c for c in my_commands[0][6:] if c.islower()]
                if len(lowercase) > 0:  # è il caso in cui entro in uno specifico file: cd #nomefile
                    print(lowercase)
                    if lowercase in root:
                        index = root.index(lowercase)
            my_commands.remove(my_commands[0])
        else:  # sto dentro una cartella e sto vedendo cosa ci sta, mi salvo riga per riga
            content_reading(index, my_commands, count)

    print(root)


if __name__ == '__main__':
    main()
