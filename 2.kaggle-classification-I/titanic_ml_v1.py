#Titanic data manual analysis, how many got survived 
import pandas as pd;
import os
os.getcwd()
#changes working directory
os.chdir("D:/Data/DataScience/Practice/titanic/")

list1 = [10,20,30]
list2 = [20,'abc',True]
print(type(list1))
print(type(list2))
list2[2] = 100 
print(list2)
list2.append('ganga')

titanic_train = pd.read_csv("train.csv")
print(type(titanic_train))
titanic_train.shape
titanic_train.info()
print(titanic_train['Sex'])
print(titanic_train.Sex)
print(titanic_train.groupby('Sex').size())
