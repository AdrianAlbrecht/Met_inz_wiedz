import math as m
import numpy as np
from random import randrange

##### Previous lesson ######
matrix = []
with open("australian.dat","r") as file:
    matrix = [list(map(lambda a: float(a),line.split())) for line in file]
    
def metryka_euklidesowa(l1, l2):
    suma = 0
    for i in range(max(len(l1),len(l2))-1):
        suma+=(l1[i]-l2[i])**2
    return m.sqrt(suma)

def grupowanie_australijczykow(lista,nr_indexu_decyzyjna,od_kogo):
    grupy = dict()
    y = lista[od_kogo]
    for x in range(1,len(lista)):
        decyzyjna = lista[x][nr_indexu_decyzyjna]
        if decyzyjna in grupy.keys():
            grupy[decyzyjna].append(metryka_euklidesowa(y, lista[x]))
        else:
            grupy[decyzyjna]=[metryka_euklidesowa(y, lista[x])]
    return grupy

def k_nn(lista,nr_indexu_decyzyjna,nowa_osoba):
    grupy = dict()
    for x in range(0,len(lista)):
        decyzyjna = lista[x][nr_indexu_decyzyjna]
        if decyzyjna in grupy.keys():
            grupy[decyzyjna].append(metryka_euklidesowa(nowa_osoba, lista[x]))
        else:
            grupy[decyzyjna]=[metryka_euklidesowa(nowa_osoba, lista[x])]      
    return grupy

def k_nn_lista(lista,nr_indexu_decyzyjna,nowa_osoba):
    grupy = []
    for x in range(0,len(lista)):
        decyzyjna = lista[x][nr_indexu_decyzyjna]
        grupy.append((decyzyjna,metryka_euklidesowa(nowa_osoba, lista[x])))    
    return grupy

grupowanie = k_nn(matrix, 14, [1,1,1,1,1,1,1,1,1,1,1,1,1,1])
grupowanie[0].sort()
grupowanie[1].sort()

def grupujemy(lista,k):
    grupy = dict()
    for element in lista:
        decyzyjna = element[0]
        if decyzyjna in grupy.keys():
            grupy[decyzyjna].append(element[1])
        else:
            grupy[decyzyjna]=[element[1]] 
    for klucz in grupy.keys():
        grupy[klucz].sort()
    for klucz in grupy.keys():
        suma = 0
        for ele in grupy[klucz][:k]:
            suma+= ele
        grupy[klucz]=suma
    return grupy
            
grupy = grupujemy(k_nn_lista(matrix, 14, [1,1,1,1,1,1,1,1,1,1,1,1,1,1]),5)

def decyzja(slownik):
    klucze = list(slownik.keys())
    ilosc = 1
    klasa = klucze[0]
    minimum = slownik[klucze[0]]
    for key in klucze[1:]:
        if minimum > slownik[key]:
            minimum = slownik[key]
            klasa = key
            ilosc=1
        elif minimum == slownik[key]:
            ilosc+=1
    if ilosc > 1:
        return 
    return klasa

###### This lesson ######
np.set_printoptions(floatmode="unique")
def metryka_euklidesowa_skalar(l1, l2):
    v1 = np.array(l1)
    v2 = np.array(l2)
    a = v2 - v1
    return m.sqrt(np.dot(a,a))
        
#print(metryka_euklidesowa_skalar(matrix[0], matrix[1])==metryka_euklidesowa(matrix[0], matrix[1]))

# - kolorki
# petla:
# - srodek masy
# - nowe kolorki względem srodka masy
# - konczymy petle, gdy kolorki sie nie zmieniaja
##### DO DOMU DOKOŃCZYĆ ######
def nauczyciel(lista):
    grupy = dict()
    for ele in lista:
        decyzyjna = ele[14]
        if decyzyjna in grupy.keys():
            grupy[decyzyjna].append(ele)
        else:
            grupy[decyzyjna]=[ele]
    matrix_without_decission = [l[:14]+[float(randrange(len(grupy.keys())))] for l in lista]
    grupy = dict()
    for ele in matrix_without_decission:
        decyzyjna = ele[14]
        if decyzyjna in grupy.keys():
            grupy[decyzyjna].append(ele)
        else:
            grupy[decyzyjna]=[ele]
    
nauczyciel(matrix)


########################## DO DOMU METODA MONTE CARLO DLA FUNKCJI (CAŁKOWANIE) ORAZ METODA PROSTOKĄTÓW/TRAPEZÓW ################################
#### y=x ####
#### y=sin ####    