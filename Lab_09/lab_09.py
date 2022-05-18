import math as m
import numpy as np

float_formatter = "{:.4f}".format
np.set_printoptions(formatter={'float_kind':float_formatter})

## PD:
## - wartosci wlasne za pomoca rozkladu QR czyli Q^T A Q

def projection(u,v):
    u_v = np.dot(u.T,v)
    u_u = np.dot(u.T,u)
    if u_u==0:
        return u
    return (u_v/u_u)*u


def matrix_len(u):
    return m.sqrt(np.dot(u.T,u))

def q_decomposition(a):
    v_list=[ [ x[i] for x in a ] for i in range(len(a[1])) ]
    u_list = []
    q = []
    
    for v in v_list:
        v = np.array(v)
        sum_proj = 0
        for u_x in u_list:
            u_x = np.array(u_x)
            sum_proj+=projection(u_x, v)
        u = v - sum_proj
        u_list.append(u)
        if matrix_len(u)==0:
            e=u
        else:
            e = (1/matrix_len(u))*u
        q.append(e)
        
    return np.array(q).T

def matrix_plus_1(a):
    q = q_decomposition(a)
    new_a = np.dot(q.T,a)
    new_a = np.dot(new_a,q)
    # if k > 1 :
    #    return matrix_eigenvalues(new_a, k-1)
    return new_a

def matrix_eigenvalues(a):
    new_a = a
    i=0
    while (np.diag(new_a)-np.dot(new_a,np.ones((len(new_a[0]),1))).T).all()>0.001 :
        new_a = matrix_plus_1(new_a)
        i=i+1
        print("A_"+str(i)+":",new_a,sep="\n")
    return new_a

def gauss(matrix):
    column_len = len(matrix.T[0])

    for x in range(column_len):
        if matrix[x][x] == 0:
            raise ZeroDivisionError() # here should use homogeneous system
            
        for y in range(column_len):
            if x != y:
                factor = matrix[y][x]/matrix[x][x]

                for z in range(column_len + 1):
                    matrix[y][z] = matrix[y][z] - factor * matrix[x][z]
    return [matrix[i][column_len]/matrix[i][i] for i in range(column_len)]
      
a=np.array([[1.,2.,3.,4.,5.],[2.,2.,3.,4.,5.],[3.,3.,3.,4.,5.],[4.,4.,4.,4.,5.],[5.,5.,5.,5.,5.]])
# a = np.array([
#     [1.,2.,0.],[0.,2.,0.],[-2.,-2.,-1.]
#     ])
# wartosci wlasne wedlug kalkulatora online
# λ_1≈19,598
# λ_2≈-3,185
# λ_3≈-0,750
# λ_4≈-0,386
# λ_5≈-0,277

print(a)
wynik = matrix_eigenvalues(a)
w_wlasne = np.diag(wynik)
print("================ WARTOSCI WLASNE ================", np.round(w_wlasne,decimals=3), sep = "\n")
print("================ WEKTORY WLASNE ================")
for x in range(len(w_wlasne)):
    print("================ λ",x,":",w_wlasne[x],"================")
    wynik_temp= a.copy()
    for i in range(len(wynik.T[0])):
        wynik_temp[i][i]-=w_wlasne[x]
    print(wynik_temp)
    wynik_temp= np.delete(wynik_temp,i,0)
    print("***wektor wlasny: ***")
    wek_wlasn = gauss(wynik_temp)+[-1.0]
    wek_wlasn = [round(y*-1,4) for y in wek_wlasn]
    print(wek_wlasn)
    
# https://matrixcalc.org/en/vectors.html#eigenvectors(%7B%7B1,2,3,4,5%7D,%7B2,2,3,4,5%7D,%7B3,3,3,4,5%7D,%7B4,4,4,4,5%7D,%7B5,5,5,5,5%7D%7D)


