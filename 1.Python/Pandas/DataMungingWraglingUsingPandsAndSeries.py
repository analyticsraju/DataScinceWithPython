import pandas as pd
import numpy as np
import os

os.chdir('D:/Data/DataScience/Practice/titanic')

type(pd)
type(np)

help(pd)

x = pd.Series([10,20,30,40,50,60])

type(x)

y = pd.Series([10,20,30,40,50],dtype=float)

type(y)

z = pd.Series([10,'Raju',20])
z[1]
type(z)

z.shape
len(z)


print(type(x[0]), type(y[0]), type(z[1]))

a = np.array([10,20,30,40,50])

type(a)

a[1]

a[::2]

b = pd.Series([10,20,30,40,50], index=['r1','r2','r3','r4','r1'])
b['r2']
b[1]
b[b>20]

c = pd.Series([10,20,30,40,50])

del(c[1])

c[1]

c[2]

d = c.reindex(range(6))

d

d[1]


titanic_train = pd.read_csv('train.csv')

titanic_train.shape
titanic_train.info()
titanic = titanic_train.head(10)
titanic_train.tail(10)
titanic_train.describe()
type(titanic_train['Sex'])
titanic['Embarked', 'Embarked'=='S']='R'
dict1 = {
   'FirstName' : pd.Series(['Surya','Nagashree','Chandra','Ramya','Keshav', 'Rajeshwari', 'Indira']),
   'LastName' : pd.Series(['narayana','Ramanath','Sekhar','Narayana','Koushik', 'Shekar','Chandra']),
   'Age' : pd.Series([40,36,70,35,12,55,52]),
   'Sex' : pd.Series(['Male','Female','Male','Female','Male','Female','Female']),
   'City' : pd.Series(['Bangalore','Dubai','Mysore','Chennai','Mumbai','Pune','Kolkata']),
   'Phone' : pd.Series([10,20,30,40,50,60,70])
}

df = pd.DataFrame(dict1)
df
df.shape
df['FirstName']
df['FullName'] = df['FirstName']+df['LastName']
df
df.shape
df['Salary']=df['Age']*5000
df
df['Salary']>20000
len(df)
df.head
df.head(2)
df.tail
df.tail(3)
df.tail(n=3)


dupdict1 = {
        'FirstName' : pd.Series(['Surya','Nagashree','Chandra','Ramya','Keshav', 'Rajeshwari', 'Indira','Surya']),
        'LastName' : pd.Series(['narayana','Ramanath','Sekhar','Narayana','Koushik', 'Shekar','Chandra','narayana']),
        'Age' : pd.Series([40,36,70,35,12,55,52,40]),
        'Sex' : pd.Series(['Male','Female','Male','Female','Male','Female','Female','Male']),
        'City' : pd.Series(['Bangalore','Dubai','Mysore','Chennai','Mumbai','Pune','Kolkata','Bangalore']),
        'Phone' : pd.Series([10,20,30,40,50,60,70,10])
}

df = pd.DataFrame(dupdict1)
df.describe()
#drop duplicates
df.drop_duplicates(inplace=True)
type(df)
#display duplicates on columns
df.loc[df.duplicated(),:]
#axis=1 below code looks for column have 'Age' are or not
test=df.drop('Age',axis=1)

#axis=0 below code looks for rows have index =2 are or not
test2=df.drop(2,axis=0)

#below is column wise duplicate identification
df.City.duplicated()

#below is row wise duplicate identification
df.duplicated()#last row is duplicated.
df.tocsv('personal.csv')


#Data mungling with pandas
gangadf = pd.read_csv('rajutest.csv')
#replace unkown with NaN
gangadf = pd.read_csv('rajutest.csv',na_values=[0,'Unknown'])

#replace unkown with NaN in column City
gangadf = pd.read_csv('rajutest.csv',na_values={'City':[0,'Unknown'],'Phone':[-40,10]})

#replace unkown with NaN in column City and Phone
gangadf = pd.read_csv('rajutest.csv',na_values={'City':[0,'Unknown','Dallas'],'Phone':[-40,10]})

gangadf.to_csv('rajuout.csv')

#remove header and index from output file.
gangadf.to_csv('rajuout.csv',index=False, header=False)



#Handling Missing Data
CompanyDF = pd.read_csv('NSE-COMP.csv')

CompanyDF.columns
CompanyDF.head(5)

df=pd.read_csv('NSE-COMP.csv', parse_dates=['Date'])
df.head(5)

df.set_index('Date', inplace=True)
df.head(5)
df.columns

#fill na with forward values
df.fillna(method='ffill', inplace=True)

#fill na with backward values
df=pd.read_csv('NSE-COMP.csv', parse_dates=['Date'])
df.head(5)
df.fillna(method='bfill', inplace=True)
df.head(5)


df=pd.read_csv('NSE-COMP.csv', parse_dates=['Date'])
df.head(5)
newdf = df.interpolate(method='linear')#default method=linear
newdf.head(5)

df=pd.read_csv('NSE-COMP.csv', parse_dates=['Date'])
df.head(5)
newdf = df.interpolate(method='time')#default method=time
newdf.head(5)

#if nan record drop, then dropna() will drop from data frame
df=pd.read_csv('NSE-COMP.csv', parse_dates=['Date'])
df.head(5)
df.dropna(inplace=True)
df.head(5)

#Data Wrangling in advence mode with repalce function.
df=pd.read_csv('NSE-COMP2.csv')
df.head(5)
df = df.replace(0,np.NaN)
df.head(5)
df.fillna(method='bfill', inplace=True)
df.head(5)

#repalce 297.5hh with 0 in entire data
df.replace('297.5hh',0, inplace=True)
df.head(5)

#repalce in D column '30dfgs1.15' with NaN in entire data
df.replace({'D':'30dfgs1.15'},np.NaN, inplace=True)
df.head(5)

#repalce 300.0,300.50 with NaN in entire data
df.replace({300.0:np.NaN, 300.50:np.NaN},inplace=True)
df.head(5)

#repalcing data with regex
df=pd.read_csv('NSE-COMP2.csv')
df.head(5)
df.replace('[A-Za-z]','',regex=True, inplace=True)
df.head(5)

ndf = pd.DataFrame ({'Student': ['Arun', 'Bhaskar', 'Chetan', 'Ramya', 'Manjula'],'Grade': ['Good','Average','Excellent','Outstanding','Poor']})
ndf.replace({'Good':'A','Average':'B'},inplace=True)




































