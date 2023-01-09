import string
from collections import OrderedDict


def copy(list):
    string = []
    for el in list: string.append(el)
    return string


def fun(list, list1):
    newlist = []
    for el in list:
        if el in list1:
            newlist.append(el)
    return newlist


def intersection(lista):
    newList = []
    while (len(lista) >= 3):
        copia = copy(lista[0])  # ho copiato la prima stringa in lista
        copia1 = copy(lista[1])
        copia2 = copy(lista[2])
        prima = []
        seconda = []
        terza = []
        [prima.append(x) for x in copia if x not in prima]  # devo togliere le ripetizioni
        [seconda.append(x) for x in copia1 if x not in seconda]
        [terza.append(x) for x in copia2 if x not in terza]
        newList.append(str(fun(terza, fun(prima, seconda))))
        del lista[0:3]

    return newList


def merge(x, y):
    z = x.copy()
    z.update(y)
    return z


def main():
    list = []
    list1 = []
    third = []

    with open("elv3", 'rt', encoding='utf-8') as f:
        for line in f:
            third.append(line.replace("\n", ""))

    common_list = []  # lista degli elementi in comune ogni tre righe senza ripetizioni
    common_list = intersection(third)
    common_list1 = []
    for el in common_list: common_list1.append(el[2])  # come posso fare meglio?
    dict = {}
    dict = OrderedDict.fromkeys(string.ascii_lowercase, range(0))
    i = 1
    for k, v in dict.items():
        dict[k] = i
        i += 1
    dict2 = OrderedDict.fromkeys(string.ascii_uppercase, range(0))
    j = 27
    for k, v in dict2.items():
        dict2[k] = j
        j += 1
    mergeddict = {}
    mergeddict = merge(dict, dict2)  # dict con key=lettere e values=numeri

    sum = 0
    for elem in common_list1: sum = sum + int(mergeddict[elem])  # cerco l'elemento della common list nelle keys
    # e rimando il relativo value
    print('sum=' + str(sum))


if __name__ == '__main__':
    main()
