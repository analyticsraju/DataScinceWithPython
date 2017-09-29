import pandas as pd
import os
import seaborn as sns

os.chdir('D:/Data/DataScience/Practice/titanic')

titanic_train = pd.read_csv('train.csv')

#EDA
titanic_train.shape
titanic_train.info

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

titanic_train['Age1'] = titanic_train['Age'].map(ageRange)
titanic_train.groupby('Age1').size()
#titanic_train.describe(['Pclass'])
#Now visualize age groups/ranges
sns.FacetGrid(data=titanic_train,row='Survived', size=8).map(sns.countplot, 'Age1').add_legend()
titanic_train.groupby(['Survived','Age1']).size()
sns.factorplot(x="Survived", hue="Age1", data=titanic_train, kind="count", size=6)
#In grapch there is much deviation in Age1 created, so I will use Title for Model Building
#Feature Creation: Creating new feature by using Name column

def titleExtractionByName(name):
    return (name.split(',')[1]).split('.')[0].strip()
    
titanic_train['Title'] = titanic_train['Name'].map(titleExtractionByName)

titanic_train.groupby('Title').size()

titleDict = {'Capt': 'Officer',
             'Col': 'Officer',
             'Don': 'Royalty',
             'Dr':'Officer',
             'Jonkheer':'Royalty',
             'Lady':'Royalty',
             'Major':'Officer',
             'Master':'Master',
             'Miss':'Miss',
             'Mlle':'Miss',
             'Mme':'Mrs',
             'Mr':'Mr',
             'Mrs':'Mrs',
             'Ms':'Mrs',
             'Rev':'Officer',
             'Sir':'Royalty',
             'the Countess':'Royalty'
             }

titanic_train['Title'] = titanic_train['Title'].map(titleDict)
titanic_train.groupby('Title').size()
#Now visualize Title groups/ranges

sns.FacetGrid(data=titanic_train,row='Survived', size=8).map(sns.countplot, 'Title').add_legend()
#With two columns FacetGrid will not help much. Better go for BiVariate-Categorical
titanic_train.groupby(['Survived','Sex']).size()
sns.factorplot(x="Survived", hue="Title", data=titanic_train, kind="count", size=6)
#In grapch there is much deviation in Title created, so I will use Title for Model Building


