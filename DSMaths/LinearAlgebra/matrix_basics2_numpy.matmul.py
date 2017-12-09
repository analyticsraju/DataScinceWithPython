import numpy as np

#############################Exercise1######################
a = np.matrix('1 2; 3 4')
a.shape
print(a)
print(type(a))
b = np.matmul(a,a)
print(b)

#############################Exercise2######################

a = np.matrix('1 2; 3 4')
a.shape
print(a)
print(type(a))
b = np.matmul(a,a)
print(b)

#############################Exercise3######################

a = np.matrix('1 2; 3 4; 5 6')
a.shape

b = np.matrix('1 2 3; 4 5 6')
b.shape

print(a)
print(b)

b = np.matmul(a,b)
print(b)

#############################Exercise4######################
