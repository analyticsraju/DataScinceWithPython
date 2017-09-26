import pandas as pd
import os
import seaborn as sns
import matplotlib.pyplot as plt

os.chdir('D:/Data/DataScience/Practice/titanic')

titanic_train = pd.read_csv('train.csv')

#EDA
titanic_train.shape
titanic_train.info

#Multivariance - Visualization
sns.FacetGrid(data=titanic_train,row='Survived',col='Sex').map(sns.countplot,'Pclass')
sns.FacetGrid(data=titanic_train,row='Survived',col='Sex',hue='Pclass').map(sns.kdeplot,'Fare')
sns.FacetGrid(data=titanic_train,row='Survived',col='Sex',hue='Fare').map(sns.kdeplot,'Age')

#Trying to visualize : See Survived ratio with Pclass, Sex, Age
sns.FacetGrid(data=titanic_train,row='Survived',col='Pclass',hue='Sex').map(sns.kdeplot, 'Age').add_legend()

#Scatter Graph
sns.FacetGrid(data=titanic_train,row='Survived',col='Sex').map(plt.scatter, 'SibSp', 'Parch')
#With Scatter graph not able to capture any data at moment.