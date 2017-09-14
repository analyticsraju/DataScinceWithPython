import numpy as np
import time

sp=time.time()
a=range(10,10000,10)

sap=time.time()
x=np.arange(10,100001,10)
y=np.arange(10,100001,10)
z=x=y
eap=time.time()
time1=(eap-sap)*1000
print(time1)

a=np.array([[10,20,30],[40,50,60],[70,80,90]])
a.sum()

b=a.sum(axis=0)
c=a.sum(axis=1)

b=np.zeros([5,5])
b=np.zeros([5,5],dtype=int)


c=np.linspace(0,2)
c=np.linspace(1,2,num=9,dytpe=np.int64)
c=np.linspace(1,5,num=10,dtype=np.int64)

dataset=np.random.random((3,3))
print(dataset)
maxval=np.max(dataset)
print(maxval)
minval=np.min(dataset)
print(minval)
maxval=np.max(dataset,axis=0)
print(maxval)
minval=np.min(dataset,axis=0)
print(minval)


dataset=np.random.random((2,2,2))
print(dataset)
maxval=np.max(dataset)
minval=np.min(dataset)

dataset=np.asarray([10,101,10],[10,101,10])
print(a)
dataset=np.mean(a)
print("mean",dataset)
dataset=np.median(a)
print("median",dataset)
dataset=np.bartlett(12)
print("mode",dataset)
dataset.size
dataset.shape
type(dataset)


from numpy.fft import fft, fftshift
import matplotlib as matplotlib
from matplotlib import pyplot as plt

window = np.bartlett(5)
print(window)
plt.plot(window)
#matplotlib.lines.Line2D object at 0x...
#plt.title("Bartlett window")
#<matplotlib.text.Text object at 0x...>
#plt.ylabel("Amplitude")
#<matplotlib.text.Text object at 0x...>
#plt.xlabel("Sample")
#<matplotlib.text.Text object at 0x...>
#plt.show()
