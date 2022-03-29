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
def srodek_masy(indeksy:list, lista:list):
    odleglosci = []
    temp_odl = 0
    for ele in indeksy:
        for ele_por in indeksy:
            temp_odl+=metryka_euklidesowa(lista[ele], lista[ele_por])
        odleglosci.append(temp_odl)
        temp_odl = 0
    mini = 0
    for i in range(1,len(odleglosci)):
        if odleglosci[mini]>odleglosci[i] :
            mini = i
    return mini
    

def nauczyciel(lista):
    grupy = dict()
    for ele in lista:
        decyzyjna = ele[14]
        if decyzyjna in grupy.keys():
            grupy[decyzyjna].append(ele)
        else:
            grupy[decyzyjna]=[ele]
    matrix_without_decission = [l[:14]+[float(randrange(len(grupy.keys())))] for l in lista]
    
    zmiany = True
    while(zmiany):
        zmiany = False
        grupy = dict()
        for i in range(len(matrix_without_decission)):
            decyzyjna = matrix_without_decission[i][-1]
            if decyzyjna in grupy.keys():
                grupy[decyzyjna].append(i)
            else:
                grupy[decyzyjna]=[i]
        new_matrix = []
        for ele in grupy.values():
            new_matrix+=ele
        srodki = []
        for lista in grupy.values():
            srodki.append(lista[srodek_masy(lista, matrix_without_decission)])
        odleglosci = []
        for ele in new_matrix:
            for sr in srodki:
                odleglosci.append(metryka_euklidesowa(matrix_without_decission[ele], matrix_without_decission[sr]))
            mini = 0
            ile = 1
            for i in range(1,len(odleglosci)):
                if odleglosci[mini]>odleglosci[i] :
                    mini = i
                    ile = 1
                elif odleglosci[mini]==odleglosci[i] :
                    ile=ile+1
            if ile==1 :
                if matrix_without_decission[ele][-1]!=matrix_without_decission[srodki[mini]][-1] :
                    matrix_without_decission[ele][-1]=matrix_without_decission[srodki[mini]][-1]
                    zmiany = True
            elif ile>1:
                matrix_without_decission[ele][-1]= None
                zmiany = True
            odleglosci=[]
    # for sr in srodki:
    #     print(matrix_without_decission[sr])
    return matrix_without_decission
        

def matrix_difference(m1,m2):
    ile = 0
    for i in range(len(m1)):
        if(m1[i]!=m2[i]):
            ile=ile+1
    return str((len(m1)-ile)/len(m1)*100)+" % pokrycia w stosunku do oryginału"
    
    
new_matrix = nauczyciel(matrix)
#print(new_matrix)
grupy = dict()
for ele in new_matrix:
      decyzyjna = ele[14]
      if decyzyjna in grupy.keys():
          grupy[decyzyjna].append(ele)
      else:
          grupy[decyzyjna]=[ele]
for key in grupy.keys():
    print("{0}: {1}".format(key,len(grupy[key])))
print(matrix_difference(matrix, new_matrix))



########################## DO DOMU METODA MONTE CARLO DLA FUNKCJI (CAŁKOWANIE) ORAZ METODA PROSTOKĄTÓW/TRAPEZÓW ################################
#### y=x ####
#### y=sin ####