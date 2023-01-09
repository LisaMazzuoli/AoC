"""None"""


def read():
    command = []
    with open("prova", "r", encoding="utf-8") as file:
        reading = [line.replace("\n", "") for line in file]
    for line in reading:
        command.append([command for command in line.split(" ")])
    return command


def signal_strength(command):
    tot_of_signal_strength = 0
    num_of_cycles = 20  # parte da 20 e poi incrementa di 40
    num_of_signals = 1  # arriva a 6
    count = 0
    signal = 1
    warn = 1
    while num_of_signals <= 6 and len(command) > 0:
        while count < num_of_cycles - 1 and len(command) > 0:
            if num_of_signals == 6:
                print(f' last count = {count}')
            if len(command[0]) == 2:
                if warn == 1:  # mi indica quando al precedente ho tagliato a metà. Il problema sarà a zero
                    count += 2
                else:
                    count += 1
                    warn = 1
                signal += int(command[0][1])
            else:
                count += 1
            del command[0]
        print(f'final signal = {signal}')
        print(f'count = {count}')
        if count == num_of_cycles - 1:
            if command[0][-1].islower():
                count += 1
                del command[0]
            else:
                count += 1
                warn = 0  # mi avvisa che ho visto solo metà di uno carico
        tot_of_signal_strength += (signal * num_of_cycles)
        num_of_signals += 1
        num_of_cycles += 40
    return tot_of_signal_strength


def main():
    """main"""
    command = read()
    tot_of_signal_strength = signal_strength(command)
    print(f'The sum of the signal strength is {tot_of_signal_strength}')


if __name__ == '__main__':
    main()
