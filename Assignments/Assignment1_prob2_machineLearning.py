
#c. Find out the pattern in the data with machine learning approach using decision tree algorithm. 
    #Find out the accuracy after submitting to kaggle.

import pandas as pd
import os
from sklearn import tree
from sklearn import model_selection

os.chdir("D:/Data/DataScience/Practice/Assignment1")

traingggdf = pd.read_csv('train.csv')

traingggdf.info()
traingggdf.shape#371,7

traingggdf.groupby(['color']).size()

    
X_train = traingggdf[['color']]

y_train = traingggdf['type']

ggg_tree = tree.DecisionTreeClassifier()

cvs = model_selection.cross_val_score(ggg_tree, X_train, y_train, cv= 10)

output = cvs.mean()
print(output)


#Data Preparation
traindummy = traingggdf[['color','hair_length']]
traindummy = traindummy
traindummy.shape

#x_traindummy = traindummy.drop(['bone_length','rotting_flesh','has_soul'],1)
#x_traindummy.shape
y_traindummy = traingggdf['type']
y_traindummy.shape

cvs = model_selection.cross_val_score(ggg_tree, traindummy, y_traindummy, cv= 10)

output = cvs.mean()
print(output) #49.99% at local model evaluation with DecisionTreeClassifier algorithm
ggg_tree.fit(traindummy, y_traindummy)

testgggdf = pd.read_csv('test.csv')
testgggdf.info()
testgggdf.shape
testdummy = testgggdf[['color','hair_length']]
testdummy.shape
#x_testdummy = testdummy.drop(['bone_length','rotting_flesh','has_soul'],1)
testgggdf['type']=ggg_tree.predict(testdummy)
testgggdf.to_csv("submission2.csv",columns=['id','type'],index=False)
#Output: Kaggle submission got 55.55%
#To get more percentage, need to analyse the data and find suitable algorithm, and then will expect good results
