import numpy as np

#############################Exercise1######################

a = [[1],
     [2],
     [3]]
b = [[1,2,3]]

c = np.array(a)
d = np.array(b)

print(c)
print(c.shape)
print(d)
print(d.shape)

#############################Exercise2######################

a = [[1,2],
     [2,3],
     [3,4]]
b = [[1,2,3],
     [4,5,6]]

c = np.array(a)
d = np.array(b)

print(c)
print(c.shape)
print(d)
print(d.shape)

e = np.matmul(c,d)

#############################Exercise3######################

x = np.array([[1,2],[3,4]])
m = np.asmatrix(x)

print(x)
print(m)
print(type(x))
print(type(m))

#############################Exercise4######################
                    