import os
import pandas as pd
from sklearn import tree
import io
import pydot
#from sklearn.ensemble import RandomForestClassifier



#returns current working directory
os.getcwd()
#changes working directory
os.chdir("D:/Data/DataScience/Practice/titanic")

titanic_train = pd.read_csv("train.csv")

#EDA
titanic_train.shape
titanic_train.info()

X_train = titanic_train[['Pclass']]
X_train.shape
y_train = titanic_train['Survived']
y_train.shape

#build the decision tree model
dt = tree.DecisionTreeClassifier()
dt.fit(X_train,y_train)

#visualize the deciion tree
dot_data = io.StringIO() 
tree.export_graphviz(dt, out_file = dot_data, feature_names = X_train.columns)
graph = pydot.graph_from_dot_data(dot_data.getvalue())[0] 
graph.write_pdf("decisionTree.pdf")


#predict the outcome using decision tree
titanic_test = pd.read_csv("test.csv")
titanic_test.shape
X_test = titanic_test[['Pclass']]
X_test.shape
titanic_test['Survived'] = dt.predict(X_test)
titanic_test.to_csv("submission.csv", columns=['PassengerId','Survived'], index=False)
