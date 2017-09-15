#Read file from csv and generate charts
import matplotlib.pyplot as plt
import csv

x=[]
y=[]

with open('C:/Users/ga311301/Downloads/NSE-WIPRO_orig.csv') as csvfile:
    print('raju')
    plots=csv.reader(csvfile,delimiter=',')
    print('raju2')
    for row in plots:
        print('raju3')
        x.append(float(row[1]))
        y.append(float(row[5]))
        print("raju4")

plt.plot(x,y, label='Loaded from file')
plt.xlabel('X-label')
plt.ylabel('Y-label')

plt.legend()
plt.title()
plt.title('Simple Data Plot from file')
plt.show()