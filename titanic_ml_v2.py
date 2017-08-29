import pandas as pd;

#list1 = [10,20,30]
#list2 = [20,'abc',True]
#print(type(list1))
#print(type(list2))
#list2[2] = 100 
#print(list2)
#list2.append('ganga')

titanic_train = pd.read_csv("D:/Data/DataScience/Practice/titanic/test.csv")
#print(type(titanic_train))
#titanic_train.shape
#titanic_train.info()
#print(titanic_train['Sex'])
#print(titanic_train.Sex)
#print(titanic_train.groupby('Sex').size())

titanic_test = pd.read_csv("D:/Data/DataScience/Practice/titanic/test.csv")
titanic_test.shape
titanic_test.info()
titanic_test['Survived'] = 0
print(titanic_test[['PassengerId', 'Survived']])
titanic_test.loc[titanic_test.Sex=='female','Survived']=1
print(titanic_test[['PassengerId', 'Survived']])
titanic_test.to_csv("D:/Data/DataScience/Practice/titanic/submission.csv",columns=['PassengerId','Survived'], index=False)
