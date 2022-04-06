import math as m
import numpy as np

def m_kowariancji(matrix):
    return np.dot(matrix.T,matrix)

def odwrotnosc_m(matrix):
    return np.linalg.inv(matrix)

def lewa_odwrotnosc(matrix):
    kow = m_kowariancji(matrix)
    odwrotnosc = odwrotnosc_m(kow)
    return np.dot(odwrotnosc,matrix.T)
  
def regresja_liniowa(matrix):
    matrix_x=np.array([[1,x[0]]for x in matrix])
    matrix_y=np.array([x[1]for x in matrix])
    lewa_odw = lewa_odwrotnosc(matrix_x)
    return np.dot(lewa_odw,matrix_y)
    

x_y=np.array([[2,1],[5,2],[7,3],[8,3]])
print(regresja_liniowa(x_y))

