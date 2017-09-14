import numpy as np

help(np)

#one dimensional array
x=np.array([1,2,3,4,5])
type(x)
print(x)
print(x.shape)
x[:5]
x[4]
x[-1]

#multi dimenstional arrays
y=np.array([[10,20,30],[20,32,3],[22,2,1]])
type(y)
y.shape
y[1][1]
y[1]
y[[0,1]]
y[-1]
y[::-1]
y.dtype

20 in y
'Raju' in y
len(y)

z=np.array([[1,2,3],[4,5,6],[7,8,9]])
z.shape
a=np.array(range(10))#starts from 0 ends 9 +1
b=np.array(range(1,10)) #starts from 1 ends 9 +1
c=np.array(range(1,10,2)) #starts from 1 ends 9 +2
d=c=np.array([range(1,10,2),range(11,20,2)])
d.shape#(2,5)
d.reshape(10).shape
d.reshape(2,2)

#retreiving and accessing only with rows
y[2]
y[[1,0]]
y[[1,2,0]]

#retrieving accessing only columns
y[::,0]
y[::,1]
y[::2]

#accessing range of elements--SLICING
#RANGE(start,end,step)
a=np.array(range(10,101,10))

#SLICING(start:end:step)
a[2:7:2]


print(50 in a)

print(50>x)
print(50<x)
print([x[50>x]])
