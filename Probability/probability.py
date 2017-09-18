import numpy.random as random
import numpy as np

#1.############
heads=0
tails=0
print(np.arange(10))
for x in range(0,100000):
    x=random.sample()
    if x>0.5:
        heads = heads+1
    else:
        tails = tails+1

print(heads)
print(tails)
#2.################
heads=0
tails=0
for x in np.arange(100000):
    x = random.randint(0,2)
    if x==0:
        heads = heads+1
    else:
        tails = tails+1
print(heads)
print(tails)
