def change_list(lista):
    Newlista = []
    for l in lista:
        if (l == 'A' or l == 'X'):
            Newlista.append(1)  # potrei usare anche switch
        elif (l == 'B' or l == 'Y'):
            Newlista.append(2)
        elif (l == 'C' or l == 'Z'):
            Newlista.append(3)
    return Newlista


def function(lista1, listamia, listasua):
    Newlist = []
    while (len(listamia) != 0 and len(listasua) != 0):  # posso pure controllarne una sola
        pos1 = lista1.index(listamia[0])
        pos = lista1.index(listasua[0])  # cerco dove sta l'elemento della lista 3 nella lista 1
        if (pos > pos1):
            Newlist.append(pos - pos1)  # sta dopo di me
        elif (pos1 > pos):
            Newlist.append(
                3 - pos1 + pos)  # sta prima di me. last pos-mia pos+sua pos-first po+1 (+1=salto per tornre indietro)
        elif (pos1 == pos):
            Newlist.append(0)  # -> 3-mia pos+sua pos
        listamia.remove(listamia[0])
        listasua.remove(listasua[0])
    return Newlist  # ritorno una lista fatta da 2,1,0


def main():
    listI = []
    listY = []
    copia = []
    with open("elv2", 'rt', encoding='utf-8') as f:
        for line in f:
            listY.append(line[0])
            listI.append(line[2])
    list1Y = change_list(listY)
    list1I = change_list(listI)
    for l in list1I: copia.append(l)
    test = [1, 2, 3]  # lista test
    sum = 0
    sum = 0
    sum = 0
    count = 0
    final_list = function(test, list1I, list1Y)
    # print(final_list)
    for elem in final_list:
        if (elem == 2): sum = sum + 6 + copia[0]
        if (elem == 1): sum = sum + copia[0]
        if (elem == 0): sum = sum + 3 + copia[0]
        copia.remove(copia[0])
    print('risultato = ' + str(sum))


if __name__ == '__main__':
    main()
