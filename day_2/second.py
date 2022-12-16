def change_list(lista):
    Newlista=[]
    for l in lista:
        if (l=='A') : Newlista.append(1) #potrei usare anche switch
        elif (l=='B') : Newlista.append(2)
        elif (l=='C') : Newlista.append(3)
    return Newlista

def change_list1(lista):
    Newlista=[]
    for l in lista:
        if (l=='X') : Newlista.append(0) #potrei usare anche switch
        elif ( l=='Y') : Newlista.append(3)
        elif (l=='Z') : Newlista.append(6)
    return Newlista


def function(lista1,listares,listasua):
    Newlist=[]
    pos=0
    while(len(listares)!=0 and len(listasua)!=0): #posso pure controllarne una sola
     pos=lista1.index(listasua[0]) #cerco dove sta l'elemento della listasua nella lista 1
     if(listares[0]==0) : #devo perdere, vado uno indietro
        if(pos==0) : Newlist.append(lista1[2])
        else : Newlist.append(lista1[pos-1])
     if (listares[0]==3) : Newlist.append(lista1[pos]) #devo stare nella sua stessa posizione per pareggiare
     if (listares[0]==6) :      #devo vincere, vado uno indietro
        if(pos==2) : Newlist.append(lista1[0])  #non posso andare indietro di uno
        else : Newlist.append(lista1[pos+1]) #posso andare indietro di 1
     listares.remove(listares[0])
     listasua.remove(listasua[0])
    return Newlist #ritorno una lista fatta da 2,1,0 che descrivono le mie mosse

def main():
    listR=[]  #lista risultati
    listY=[]
    copia=[]
    with open("elv2", 'rt', encoding='utf-8') as f:
      for line in f:
        listY.append(line[0])
        listR.append(line[2])
    list1Y=change_list(listY)
    list1R=change_list1(listR)
    #print(list1Y)
    #print(list1R)
    for l in list1R : copia.append(l)
    test=[1,2,3] #lista test
    sum=0
    #count=0
    final_list=function(test,list1R,list1Y) #torno la lista delle mie mosse
    #print(final_list)
    for elem in final_list:
        sum=sum + elem + copia[0]
        #print('sum=' + str(sum))
        copia.remove(copia[0])
    print('risultato = ' + str(sum))

if __name__ == '__main__':
         main()