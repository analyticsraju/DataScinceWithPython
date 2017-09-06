import pandas as pd
import os
from sklearn import tree
from sklearn import model_selection

os.getcwd()
os.chdir("D:/Data/DataScience/Practice/Assignment1")

traindf = pd.read_csv('train.csv')
print(type(traindf))

#a. Apply random predictions/majority based prediction to each observation 
#and 
#find out how much accurate your predictions are by submitting to kaggle?
traindf['type']
traindf.groupby(['type']).size()
traindf.groupby(['color','type']).size()
print(traindf.groupby('type').mean())

testdf = pd.read_csv('test.csv')
type(testdf)
print(testdf)
testdf['type']='Ghoul'
print(testdf)
testdf.to_csv("submission.csv",columns=['id','type'], index=False)
    #Output: At Koggle submission got around 33%


#b. Find out the pattern in the data manually and then hard-code the logic. 
#Find out the accuracy by submitting to kaggle.
traindf['type']
traindf.groupby(['type']).size()
traindf.groupby(['color','type']).size()
print(traindf.groupby('type').mean())

testdf = pd.read_csv('test.csv')
type(testdf)
print(testdf)
testdf['type']='Ghoul'
testdf.loc[testdf.color=='white', 'type']='Ghost'
testdf.loc[testdf.color=='clear', 'type']='Goblin'
print(testdf)
testdf.to_csv("submission.csv",columns=['id','type'], index=False)
    #Output: At Koggle submission got around 34%

