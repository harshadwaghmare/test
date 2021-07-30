#!/usr/bin/python3

def secondlargest(lista):
    smax = 0
    for i in lista:
        if (i > smax) and (i != max(lista)):
            smax = i
    return smax

def bsecondlargest (lista):
    lista.sort()
    return lista[-2]

def swapfirstlast (lista):
    lista[0], lista[-1] = lista[-1], lista[0]
    for i in lista:
        print (i)

if __name__ == '__main__':
    a = [1,2,3,4,5]
   # print (bsecondlargest(a))
    swapfirstlast(a)