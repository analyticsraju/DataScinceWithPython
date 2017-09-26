import pandas as pd
import os

os.chdir('D:/Data/DataScience/Practice/titanic')

titanic_train = pd.read_csv('train.csv')

#EDA
titanic_train.shape
titanic_train.info

def ageRange(age):
    ageRange
    if(age>0 & age<=10):
        ageRange='Child'
    if(age>10 & age<=30):
        ageRange='Young'
    if(age>30 & age<=50):
        ageRange='Adult'
    if(age>45 & age<=80):
        ageRange='Old'

lambda .map()
