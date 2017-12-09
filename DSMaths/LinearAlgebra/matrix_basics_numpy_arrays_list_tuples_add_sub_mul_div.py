import numpy as np

#############################Exercise1######################
a=[[1,0],
   [0,1]]

b=[[4,1],
   [2,2]]

#matri multiplication
type(a)
c=np.matmul(a,b)

#addition
d=a+b

#substraction
e=a-b#getting error

##Conclusion
#Only lists can not handle matrix operations.

#############################Exercise2######################
#I am trying with numpy arrays, lists for matrix operations
m1 = np.array([[1,0],
               [0,1]])

m2 = np.array([[4,1],
               [2,2]])

#matrix operations with 
m3 = m1*m2
m4 = m1+m2
m5 = m1/m2
m6 = m1-m2

#############################Exercise3######################
#now I am trying with numpy arrays, lists, tuples*** for matrix operations
t = ([1,0], [0,1])
type(t)

t1 = np.array(([1,0],
               [0,1]))

n1 = np.array([[4,1],
               [2,2]])
#matrix operations
n2 = t1*n1
n3 = t1+n1
n4 = t1/n1
n5 = t1-n1
n5.shape
#############################Exercise4######################
#now comparing Exercise2 and Exercise3 results
m3 == n2
m4 == n3
m5 == n4
m6 == n5

##Conclusion on numpy, arrays, list, tuples
#Matrics handling efficiently with numpy, arrays(list,tuples)

