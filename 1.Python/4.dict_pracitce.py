#dict basics
fares = {10,20,30}
print(type(fares))#set

titanicData = {'id':(5,7,10), 'fare':(10,20,30), 'Sex':['Male','Female','NA']}
print(type(titanicData))

#tuple accessing
titanicData['id']
titanicData['Sex']

titanicData['pid']#if acces like this will throw error
titanicData.get('pid')#no error
type(titanicData.get('pid'))#NoneType. Means no data with 'pid' in titanicData variable.

#Padas.dataframe and dict

import pandas as pd

titanicDF = pd.DataFrame(titanicData)
type(titanicDF)
titanicDF['id']
print(titanicDF['id'])#int
titanicDF['Sex']
type(titanicDF['Sex'])#Series
