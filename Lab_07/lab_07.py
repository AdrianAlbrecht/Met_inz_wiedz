import math as m
import numpy as np

float_formatter = "{:.4f}".format
np.set_printoptions(formatter={'float_kind':float_formatter})


def projection(u,v):
    u_v = np.dot(u.T,v)
    u_u = np.dot(u.T,u)
    if u_u==0:
        return u
    return (u_v/u_u)*u


def matrix_len(u):
    return m.sqrt(np.dot(u.T,u))


# given
a=np.array([[2,0],[0,1],[1,2]])

# when
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
    
q = np.array(q).T
r = np.dot(q.T,a)

new_a = np.dot(q,r)
        

# then
print(q,r,new_a,sep="\n\n")
