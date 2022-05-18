import numpy as np
import math as m

#macierz ortagonalna

a = np.array([[1.,1.,1.,1.,1.,1.,1.,1.],
              [1.,1.,1.,1.,-1.,-1.,-1.,-1],
              [1.,1.,-1.,-1.,0.,0.,0.,0.],
              [0.,0.,0.,0.,1.,1.,-1.,-1.],
              [1.,-1.,0.,0.,0.,0.,0.,0.],
              [0.,0.,1.,-1.,0.,0.,0.,0.],
              [0.,0.,0.,0.,1.,-1.,0.,0.],
              [0.,0.,0.,0.,0.,0.,1.,-1.]])

b = np.dot(a,a.T)
c = []
temp = 0
for row in a:
    temp=0
    for y in row:
        temp+=abs(y)
    c.append(temp)
#print(b)
print(all(c==np.diag(b)))

#macierz ortonormalna
d = []
for i in range(len(a[0])):
    # row = []
    # for x in a[i]:
    #     row.append(x/m.sqrt(c[i]))
    # d.append(row)
    d.append(a[i]*(1/m.sqrt(c[i])))
d = np.array(d) #macierz ortonormalna
print(d.T) #transpozycja ortonormalnej
print(np.linalg.inv(d)) #odwrotna ortonormalna
print(np.dot(d,np.linalg.inv(d))) #d * d^-1
print(np.diag([1.,1.,1.,1.,1.,1.,1.,1.]).all()==np.dot(d,np.linalg.inv(d)).all())

#zamiana baz
ones = np.diag([1.,1.,1.,1.,1.,1.,1.,1.])
va=np.array([8.,6.,2.,3.,4.,6.,6.,5.])
vb=np.dot(d,va) #bo d już jest transponowane
print(vb)