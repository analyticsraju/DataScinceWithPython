import pandas as pd
import numpy as np
import os

os.chdir('D:/Data/DataScience/Practice/titanic')

type(pd)
type(np)

help(pd)

x = pd.Series([10,20,30,40,50,60])

type(x)

y = pd.Series([10,20,30,40,50],dtype=float)

type(y)

z = pd.Series([10,'Raju',20])

type(z)

z.shape
len(z)


print(type(x[0]), type(y[0]), type(z[1]))

a = np.array([10,20,30,40,50])

type(a)

a[1]

a[::2]

b = pd.Series([10,20,30,40,50], index=['r1','r2','r3','r4','r1'])
b['r2']
b[1]
b[b>20]

c = pd.Series([10,20,30,40,50])

del(c[1])

c[1]

c[2]

d = c.reindex(range(6))

d

d[1]


titanic_train = pd.read_csv('train.csv')

titanic_train.shape
titanic_train.info()
titanic_train.head(10)
titanic_train.tail(10)
titanic_train.describe()
