#https://docs.scipy.org/doc/numpy-dev/user/quickstart.html
#All below examples are at above url

import numpy as np

x=np.arange(10)

x=np.arange(1,10,0.5, dtype=float)

print(x.size)

print(len(x))

x.nbytes

x.itemsize

#dtype=np.float32
y=np.arange(1,10,0.5, dtype=np.float32)

print(y.size)

print(len(y))

y.nbytes

y.itemsize



