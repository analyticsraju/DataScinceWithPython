import numpy as np

#############################Exercise1######################

x = np.array([2,3])
y = np.array([1,2])

z1 = np.dot(x,y) #====> z1 = x.y = |x|.|y|.cosTeta ==>Scalar==>Dot Product
z2 = np.cross(x,y) #====> z2 = x*y = |x|*|y|.sinTeta ==>Cross Product
print(z1)
print(type(z1))
print(z2)
print(type(z2))

#############################Exercise2######################
a = np.array([0,0,1])
b = np.array([0,1,0])

c = np.dot(a,b)
d = np.cross(a,b)
print(c)
print(d)
print(type(c))

#############################Exercise3######################
a = np.array([0,0,1])
b = np.array([0,1,0])

c = np.dot(a,b)
d = np.cross(a,b)
print(c)
print(d)
print(type(c))







