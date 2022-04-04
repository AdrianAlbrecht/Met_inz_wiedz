import math as m

matrix = []
with open("../Lab_03/australian.dat","r") as file:
    matrix = [list(map(lambda a: float(a),line.split())) for line in file]
    
# srednia arytmetyczna, wariancja, odchylenie standardowe

def srednia_aryt(lista):
    suma = 0.0
    for x in lista:
        suma+=x
    return float(suma/(float(len(lista))))

def wariancja(lista):
    srednia = srednia_aryt(lista)
    suma= 0.0
    for x in lista:
        suma+= (x - srednia)**2
    return float(suma/(float(len(lista))))

def odchylenie_std(lista):
    return m.sqrt(wariancja(lista))


# wersja jak ja to zrozumiałem
matrix_1 = [x[1] for x in matrix] #list_of_index_1_of_matrix
print(srednia_aryt(matrix_1))
print(wariancja(matrix_1))
print(odchylenie_std(matrix_1))

print("============ v 2.0 =================")
# wersja według wykładu????
matrix_2 = [x[:14] for x in matrix] #matrix without decission
print(srednia_aryt(matrix_2[0]))
print(wariancja(matrix_2[0]))
print(odchylenie_std(matrix_2[0]))
