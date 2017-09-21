import numpy as np
from numpy import pi

a = np.array([0,1,2])
print(type(a[0][0]))

b=np.array([[1,2],[3,4]],dtype=complex)
print(type(b[0][0]))

c=np.zeros([2,3])

d=np.ones([2,3])

e=np.empty((2,3))

f=np.ones([2,3,4])
print(type(f))

g=np.ones([2,3,4,5])


h=np.arange(10,30,5)

i=np.array(range(0,5,1.5))#range float not accepted

j=np.arange(0,2,0.2)

#import pi 
k=np.linspace(0,2,9)

l=np.linspace(0,2*pi,100)
np.linalg()
