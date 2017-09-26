import pandas as pd
import os
import seaborn as sns


os.chdir('D:/Data/DataScience/Practice/titanic')

titanic_train = pd.read_csv('train.csv')

#EDA
titanic_train.shape
titanic_train.info

#statistical exploration
pd.crosstab(index=titanic_train['Survived'],columns=titanic_train['Sex'])
pd.crosstab(index=titanic_train['Survived'],columns=titanic_train['Pclass'])

#BiVariate - Categorical data visualization

sns.factorplot(x='Survived',hue='Sex',data=titanic_train,kind='count',size=6)
#1. Considering 'Sex' for Model building

sns.factorplot(x='Survived',hue='Pclass',data=titanic_train,kind='count',size=6)
#2. Considering 'Pclass' for Model Building

sns.factorplot(x='Survived',hue='Embarked',data=titanic_train,kind='count',size=6)
#3. Considering 'Embarked' for model building

sns.factorplot(x='Fare',hue='Survived',data=titanic_train,kind='box',size=6)
#4. Not sure from this factorplot, its not clear to me.

#BiVariate - Continuous & Categorical visualization
#1. Generating visualtion for Survived vs Fare
sns.FacetGrid(data=titanic_train,row='Survived',size=8).map(sns.kdeplot, 'Fare').add_legend()
#1. Here Based on Fare Survival got better. Considering Fare column for model building

#2. Generating visualtion for Survived vs Pclass
sns.FacetGrid(data=titanic_train,row='Survived',size=8).map(sns.kdeplot, 'Pclass').add_legend()
#2. Considering Pclass column for Model Building

#3. Generating visualtion for Survived vs Parch
sns.FacetGrid(data=titanic_train,row='Survived',size=8).map(sns.kdeplot, 'Parch').add_legend()
#3. Not sure at the moment, not considering for model building

#4. Generating visualtion for Survived vs Age
sns.FacetGrid(data=titanic_train,row='Survived',size=8).map(sns.kdeplot, 'Age').add_legend()
#4. Age visualiztion not giving correct information, not considering Age at moment.

###############Summary#################
#From BiVariate Considered Columns Survived vs [Sex,Pclass,Embarked,Fare]