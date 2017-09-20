import pandas as pd
from sklearn import tree
from sklearn import model_selection
import os

os.chdir('D:/Data/DataScience/Practice/titanic')

titanic_train = pd.read_csv("train.csv")

#explore the dataframe
titanic_train.shape
titanic_train.info()

#convert categorical columns to one-hot encoded columns
titanic_train1 = pd.get_dummies(titanic_train, columns=['Sex','Pclass','Embarked'])
titanic_train1.shape
titanic_train1.info()

X_train = titanic_train1.drop(['PassengerId','Name','Age','Ticket','Cabin','Survived'], axis=1, inplace=False)
X_train.shape
X_train.info()
Y_train = titanic_train['Survived']


dt = tree.DecisionTreeClassifier(random_state=2017)
param_grid = {'criterion':['entropy','gini'],'max_depth':[1,2,3,4,5,6,7,8,9,10,11,12], 'min_samples_split':[2,3,4,5,6,7,8,9,10,11,12,20,25]}
dt_grid = model_selection.GridSearchCV(dt, param_grid, cv=10, n_jobs=5)
dt_grid.fit(X_train, Y_train)
print(dt_grid.grid_scores_)
print(dt_grid.best_estimator_)
print(dt_grid.best_score_)
print(dt_grid.score(X_train, Y_train))


titanic_test = pd.read_csv('test.csv')
titanic_test.shape
titanic_test.info()

#fill the missing value for fare column
titanic_test.loc[titanic_test['Fare'].isnull() == True, 'Fare'] = titanic_test['Fare'].mean()

titanic_test1 = pd.get_dummies(titanic_test, columns=['Sex','Pclass','Embarked'])
titanic_test1.shape
titanic_test1.info()

X_test = titanic_test1.drop(['PassengerId','Name','Age','Ticket','Cabin'], axis=1, inplace=False)
X_test.shape
X_test.info()

titanic_test['Survived'] = dt_grid.predict(X_test)

titanic_test.to_csv('submission.csv', columns=['PassengerId','Survived'],index=False)
