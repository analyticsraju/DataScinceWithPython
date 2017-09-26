import pandas as pd
import os
import seaborn as sns

os.chdir('D:/Data/DataScience/Practice/titanic')

titanic_train = pd.read_csv('train.csv')

#EDA
titanic_train.shape
titanic_train.info

#statistical exploration
titanic_train['Survived'].describe()
pd.crosstab(index=titanic_train['Survived'],columns="count")
pd.crosstab(index=titanic_train['Sex'],columns="count")
pd.crosstab(index=titanic_train['Pclass'],columns="count")

#visualization exploration
#UniVariate - categorical features visualization
plot = sns.countplot(x='Survived', data=titanic_train)
plot = sns.countplot(x='Pclass', data=titanic_train)

#Univariance - countinuous feature visualization
print(titanic_train['Fare'].describe())

sns.boxplot(x='Fare', data=titanic_train)
sns.distplot(titanic_train['Fare'])
sns.distplot(titanic_train['Fare'], bins=20, rug=True, kde=False)
sns.distplot(titanic_train['Fare'], bins=100, kde=False)
sns.kdeplot(data=titanic_train['Fare'])
sns.kdeplot(data=titanic_train['Fare'],shade=True)
