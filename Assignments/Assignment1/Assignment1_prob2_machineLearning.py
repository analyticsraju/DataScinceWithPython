
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
#Approach-1
traingggdf.groupby(['color']).size()
X_train = traingggdf[['color']]
y_train = traingggdf['type']
ggg_tree = tree.DecisionTreeClassifier()
cvs = model_selection.cross_val_score(ggg_tree, X_train, y_train, cv= 10)
output = cvs.mean()
print(output)

#Approach-2
#Data Preparation
x_traindummy2 = traingggdf[['color','hair_length']]
x_traindummy2.shape
y_traindummy2 = traingggdf['type']
y_traindummy2.shape
cvs2 = model_selection.cross_val_score(ggg_tree, x_traindummy2, y_traindummy2, cv= 10)
output2 = cvs2.mean()
print(output2)#50.5
ggg_tree.fit(x_traindummy2, y_traindummy2)

testgggdf2 = pd.read_csv('test.csv')
testgggdf2.info()
testgggdf2.shape
testdummy2 = testgggdf2[['color','hair_length']]
testdummy2.shape
#x_testdummy = testdummy.drop(['bone_length','rotting_flesh','has_soul'],1)
testgggdf2['type']=ggg_tree.predict(testdummy2)
testgggdf2.to_csv("submission2.csv",columns=['id','type'],index=False)
#Kaggle submission score 55.55

#Approach-3
x_traindummy3 = traingggdf[['color','hair_length','bone_length','has_soul','rotting_flesh']]
x_traindummy3.shape
y_traindummy3 = traingggdf['type']
y_traindummy3.shape
cvs3 = model_selection.cross_val_score(ggg_tree,x_traindummy3,y_traindummy3,cv=10)
output3 = cvs3.mean()
print(output3)#54.29#61.26#66.83
ggg_tree.fit(x_traindummy3, y_traindummy3)

testgggdf3 = pd.read_csv('test.csv')
testgggdf3.info()
testgggdf3.shape
testdummy3 = testgggdf3[['color','hair_length','bone_length','has_soul','rotting_flesh']]
testdummy3.shape
testgggdf3['type'] = ggg_tree.predict(testdummy3)
testgggdf3.to_csv("submission3.csv", columns=['id','type'], index=False)
#Kaggle submission score 65.59