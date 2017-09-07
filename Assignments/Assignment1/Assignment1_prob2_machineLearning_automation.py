#c. Find out the pattern in the data with machine learning approach using decision tree algorithm. 
    #Find out the accuracy after submitting to kaggle.

import pandas as pd
import os
from sklearn import tree
from sklearn import model_selection

os.chdir("D:/Data/DataScience/Practice/Assignment1")

traindf = pd.read_csv('train.csv')

traindf.info()
traindf.shape#371,7


for index in range(0 ,371):
    if(traindf.iloc[index,5])=='clear':
        traindf.iloc[index,5]=1
    if(traindf.iloc[index,5])=='green':
        traindf.iloc[index,5]=2
    if(traindf.iloc[index,5])=='black':
        traindf.iloc[index,5]=3
    if(traindf.iloc[index,5])=='white':
        traindf.iloc[index,5]=4
    if(traindf.iloc[index,5])=='blue':
        traindf.iloc[index,5]=5
    if(traindf.iloc[index,5])=='blood':
        traindf.iloc[index,5]=6
    #else:
        #print('???',traindf.iloc[index,5])
    
    if(traindf.iloc[index,6])=='Goblin':
        traindf.iloc[index,6]=1
    if(traindf.iloc[index,6])=='Ghoul':
        traindf.iloc[index,6]=2
    if(traindf.iloc[index,6])=='Ghost':
        traindf.iloc[index,6]=3
    else:
        print('???',type(traindf.iloc[index,6]))


type(traindf.color)
type(traindf.type)

x_traindummy4 = traindf[['color','hair_length','bone_length','has_soul','rotting_flesh']]
type(x_traindummy4)
x_traindummy4.shape
y_traindummy4 = traindf[['type']]
type(y_traindummy4)
y_traindummy4 = list(traindf.type.values)
type(y_traindummy4)
#y_traindummy4.shape
ggg_tree = tree.DecisionTreeClassifier()
cvs4 = model_selection.cross_val_score(ggg_tree,x_traindummy4,y_traindummy4,cv=10)
output4 = cvs4.mean()
print(output4)#54.29#61.26#66.83
ggg_tree.fit(x_traindummy4, y_traindummy4)






testdf4 = pd.read_csv('test.csv')
testdf4.info()
testdf4.shape

for index in range(0 ,529):
    if(testdf4.iloc[index,5])=='clear':
        testdf4.iloc[index,5]=1
    if(testdf4.iloc[index,5])=='green':
        testdf4.iloc[index,5]=2
    if(testdf4.iloc[index,5])=='black':
        testdf4.iloc[index,5]=3
    if(testdf4.iloc[index,5])=='white':
        testdf4.iloc[index,5]=4
    if(testdf4.iloc[index,5])=='blue':
        testdf4.iloc[index,5]=5
    if(testdf4.iloc[index,5])=='blood':
        testdf4.iloc[index,5]=6

testdummy4 = testdf4[['color','hair_length','bone_length','has_soul','rotting_flesh']]
testdummy4.shape
testdf4['type'] = ggg_tree.predict(testdummy4)


for index in range(0 ,529):
    if(testdummy4.iloc[index,6])==1:
        testdummy4.iloc[index,6]='Goblin'
    if(testdummy4.iloc[index,6])==2:
        testdummy4.iloc[index,6]='Ghoul'
    if(testdummy4.iloc[index,6])==3:
        testdummy4.iloc[index,6]='Ghost'
    else:
        print('???',type(testdummy4.iloc[index,6]))

testdummy4.to_csv("submission4.csv", columns=['id','type'], index=False)
#Kaggle submission score 65.59