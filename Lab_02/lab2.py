import math as m

miasta = ["Warszawa","Gdańsk","Łódź","Poznań","Ełk","Sosnowiec"]

print(list(map(lambda a:a[0:3], miasta)))

matrix = []
## normal for
# with open("australian.dat","r") as file:
#     matrix = []
#     for line in file:
#         line = line.split("\n")
#         data = line[0].split()
#         matrix.append(data)
# print(matrix)
    
# python comprahension 
with open("australian.dat","r") as file:
    matrix = [list(map(lambda a: float(a),line.split())) for line in file]
    
#print(matrix)

def metryka_euklidesowa(l1, l2):
    suma = 0
    for i in range(len(l1)-1):
        suma+=(l1[i]-l2[i])**2
    return m.sqrt(suma)
    
print(metryka_euklidesowa(matrix[0],matrix[1]))
print(metryka_euklidesowa(matrix[0],matrix[2]))
print(metryka_euklidesowa(matrix[0],matrix[3]))

############## DO DOMU ################
# Funkcja, która policzy odległosc kazdego objectu do objectu 0
# pogrupować wględem klasy decyzyjnej (ostatni atrybut) do słownika { klasa decyzyjna: lista wartosci}

def grupowanie_australijczykow(lista,nr_indexu_decyzyjna):
    grupy = dict()
    y = lista[0]
    for x in range(1,len(lista)):
        decyzyjna = lista[x][nr_indexu_decyzyjna]
        if decyzyjna in grupy.keys():
            grupy[decyzyjna].append(metryka_euklidesowa(y, lista[x]))
        else:
            grupy[decyzyjna]=[metryka_euklidesowa(y, lista[x])]
    return grupy

print("===== PD ======")
print(grupowanie_australijczykow(matrix,14))
        