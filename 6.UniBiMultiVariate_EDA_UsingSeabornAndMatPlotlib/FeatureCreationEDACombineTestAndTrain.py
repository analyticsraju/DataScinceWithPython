import pandas as pd
import os
import seaborn as sns
from sklearn import tree
from sklearn import preprocessing
from sklearn import model_selection


os.chdir('D:/Data/DataScience/Practice/titanic')

titanic_train = pd.read_csv('train.csv')
titanic_test = pd.read_csv('test.csv')
titanic_train.info()
titanic_test['Survived'] = None
titanic_test.info()

titanicAll = pd.concat([titanic_train,titanic_test])
titanicAll.info()

#EDA
titanicAll.shape
titanicAll.info

#create an instance of Imputer class with required arguments
mean_imputer = preprocessing.Imputer()
#compute mean of age and fare respectively
mean_imputer.fit(titanic_train[['Age','Fare']])
#fill up the missing data with the computed means 
titanicAll[['Age','Fare']] = mean_imputer.transform(titanicAll[['Age','Fare']])

#Feature Considered Till now Age, Fare, Survived
#Feature Creation: Creating new feature with Age column to see visualization. To find differences in age groups.
def ageRange(age):
    ageRange=''
    if age<=10:
        ageRange='Child'
    elif age<=30:
        ageRange='Young'
    elif(age<=50):
        ageRange='Adult'
    elif(age<=80):
        ageRange='Old'
    elif(age<=100):
        ageRange='Oldest'
    return ageRange

titanicAll['Age1'] = titanicAll['Age'].map(ageRange)
titanicAll.groupby('Age1').size()
#titanic_train.describe(['Pclass'])
#Now visualize age groups/ranges
sns.FacetGrid(data=titanicAll,row='Survived', size=8).map(sns.countplot, 'Age1').add_legend()
titanicAll.groupby(['Survived','Age1']).size()
sns.factorplot(x="Survived", hue="Age1", data=titanicAll, kind="count", size=6)
#In grapch there is much deviation in Age1 created, so I will use Title for Model Building
#Features Considered Till now (+Age1, Fare, Survived)(-Age)
#Feature Creation: Creating new feature by using Name column

def titleExtractionByName(name):
    return (name.split(',')[1]).split('.')[0].strip()
    
titanicAll['Title'] = titanicAll['Name'].map(titleExtractionByName)

titanicAll.groupby('Title').size()

titleDict = {'Capt': 'Officer',
             'Col': 'Officer',
             'Dr':'Officer',
             'Major':'Officer',
             'Rev':'Officer',
             'Sir':'Royalty',
             'the Countess':'Royalty',
             'Don': 'Royalty',
             'Jonkheer':'Royalty',
             'Lady':'Royalty',
             'Master':'Master',
             'Miss':'Miss',
             'Mlle':'Miss',
             'Mrs':'Mrs',
             'Mme':'Mrs',
             'Ms':'Mrs',
             'Mr':'Mr'
             }

titanicAll['Title'] = titanicAll['Title'].map(titleDict)
titanicAll.groupby('Title').size()
#Now visualize Title groups/ranges

sns.FacetGrid(data=titanicAll,row='Survived', size=8).map(sns.countplot, 'Title').add_legend()
#With two columns FacetGrid will not help much. Better go for BiVariate-Categorical
titanicAll.groupby(['Survived','Sex']).size()
sns.factorplot(x="Survived", hue="Title", data=titanicAll, kind="count", size=6)
#In grapch there is much deviation in Title created, so I will use Title for Model Building
#Features Considered Till now (+Age1,+Title, Fare, Survived)(-Age,-Name)

#Exploration of SibSp(Sibling Spuse) and Parch(Parent Children) - Here we need domain knowledge.
titanicAll['SibSp'].describe()
titanicAll['Parch'].describe()
#Subling, Spouse, Parent Children are related to family, for a given family how many are travelling.
#Lets create a Feature 'Family', add(SibSp, Parch)
titanicAll['Family'] = titanicAll['SibSp']+titanicAll['Parch']
titanicAll['Family'].describe()
#Now Family Feature is seems continuous
#Lets make categorical

def familySize(family):
    familySize = ''
    if(family<=1):
        familySize = 'Single'
    elif(family<=3):
        familySize = 'Small'
    elif(family<=5):
        familySize = 'Medium'
    else:
        familySize = 'Large'
    return familySize

titanicAll['FamilySize'] = titanicAll['Family'].map(familySize)
#Now Lets visualize 
titanicAll.groupby(['FamilySize','Survived']).size()
sns.factorplot(x="Survived", hue="FamilySize", data=titanicAll, kind="count", size=6)
#From Graph there is much deviation between family sizes, so Feature 'FamilySize' is important feature, So I am considering for Model building.
#Features Considered Till now (+Age1,+Title,+FamilySize, Fare, Survived)(-Age,-Name,-SibSp,-Parch,-Family)

titanicAll.describe()

#convert categorical columns to one-hot encoded columns
titanic1 = pd.get_dummies(titanicAll, columns=['Sex','Pclass','Embarked', 'Age1', 'Title', 'FamilySize'])
titanic1.shape
titanic1.info()

#dropping us used Feautres from train data
titanic2 = titanic1.drop(['PassengerId','Name','Age','Ticket','Cabin','Survived','SibSp','Parch'], axis=1, inplace=False)
titanic2.info()
X_train = titanic2[0:titanic_train.shape[0]]
X_train.shape
X_train.info()
y_train = titanic_train['Survived']

tree_estimator = tree.DecisionTreeClassifier(random_state=2017)
dt_grid = {'criterion':['gini','entropy'], 'max_depth':list(range(3,10))}
grid_tree_estimator = model_selection.GridSearchCV(tree_estimator, dt_grid, cv=10)
grid_tree_estimator.fit(X_train, y_train)
print(grid_tree_estimator.grid_scores_)
print(grid_tree_estimator.best_score_)#83.16
print(grid_tree_estimator.best_params_)#
print(grid_tree_estimator.score(X_train, y_train))#84.39
#Less Bias and Variance between cv score and train score, so Model is not overfit. Hence Model is good

##################
#############################
X_test = titanic2[titanic_train.shape[0]:]
X_test.shape
X_test.info()

titanic_test['Survived'] = grid_tree_estimator.predict(X_test)

titanic_test.to_csv('submission.csv', columns=['PassengerId','Survived'],index=False)

