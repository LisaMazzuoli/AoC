import string
from collections import OrderedDict


def copy(list):
    string = []
    for el in list: string.append(el)
    return string


def intersection(list1, list2):
    newList = []
    for element in list1:
        copia = copy(element)
        copia1 = copy(list2[0])  # ho copiato la prima stringa in lista
        copiares = []
        copia1res = []
        [copiares.append(x) for x in copia if x not in copiares]  # devo togliere le ripetizioni
        [copia1res.append(x) for x in copia1 if x not in copia1res]
        for el in copiares:
            if el in copia1res:
                newList.append(el)
        list2.remove(list2[0])

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
            third.append(line)
    for line in third:
        list.append(line[:len(line) // 2])
        list1.append(line[len(line) // 2:])

    common_list = []  # lista degli elementi in comune senza ripetizioni
    common_list = intersection(list, list1)

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
    for keys in mergeddict: print(keys)
    for el in common_list: print(el)
    sum = 0

    for elem in common_list: sum = sum + int(mergeddict[elem])  # cerco l'elemento della common list nelle keys
                                                                # e rimando il relativo value
    print('sum=' + str(sum))


if __name__ == '__main__':
    main()
