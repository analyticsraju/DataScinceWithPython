import pandas as pd;
import os
os.getcwd()
#changes working directory
os.chdir("D:/Data/DataScience/Practice/titanic/")

titanic_test = pd.read_csv("test.csv")
titanic_test.shape
titanic_test.info()
titanic_test['Survived'] = 0
print(titanic_test[['PassengerId', 'Survived']])
titanic_test.loc[titanic_test.Sex=='female','Survived']=1
titanic_test.loc[titanic_test.Sex=='male','Survived']=0
print(titanic_test[['PassengerId', 'Survived']])
titanic_test.to_csv("D:/Data/DataScience/Practice/titanic/submission.csv",columns=['PassengerId','Survived'], index=False)
