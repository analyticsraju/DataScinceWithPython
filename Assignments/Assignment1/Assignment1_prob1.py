import pandas as pd
import os

os.getcwd()
#a.Load the data set and make it a dataframe called rain.df.
os.chdir("D:/Data/DataScience/Practice/Assignment1")
rain_df = pd.read_csv('train2.csv')
pd.
#b.How many rows and columns does rain.df have? How do you know? (If there are not 5070 rows and 27 columns, you did something wrong in the first part of the problem.)
rain_df.shape
rain_df.info()
#c.What command would you use to get the names of the columns of rain.df? What are those names?
rain_df[:0]
#d. What command would you use to get the value at row 2, column 4? What is the value?
rain_df.iloc[0,3]
#e. What command would you use to display the whole second row? What is the content of that row?
rain_df.iloc[0]
#f. Create a new column called daily which is the sum of the 24 hourly columns
print(rain_df)
fareSum = sum(rain_df['Fare'])
print(fareSum)
rain_df['new'] = fareSum
print(rain_df)
