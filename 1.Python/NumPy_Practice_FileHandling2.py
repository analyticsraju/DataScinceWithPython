#File reading
import os
import numpy as np

os.getcwd
os.chdir('C:/Users/ga311301/Downloads/')

fd=open('raju.txt','a')
print(fd.readlines())

a,b=10,20
a,b,c=10,20.5,'raju'

Date,Open,High,Low,Last,Close,Total,Turnover=np.loadtxt('NSE-WIPRO_orig.csv',delimiter=',',unpack=True,dtype='str')

print(type(Date),type(Open),type(High),type(Low),type(Last),type(Close),type(Total),type(Turnover))

print(Date[5])
x=0
for eachclose in Close:
    saveline=Open[x]+','+Close[x]+'\n'
    print(saveline)
    x=x+1
    fd.write(saveline)
