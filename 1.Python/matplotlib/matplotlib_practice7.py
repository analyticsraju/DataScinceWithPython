#Sample plot of Bar style example-4
import matplotlib.pyplot as plt

x=[1,2,3,4,5,6,7,8,9]
y=[3,5,4,6,9,3,1,7,8]

plt.scatter(x,y,label='Scatter', color='c',marker='o')

plt.xlabel('X-label')
plt.ylabel('Y-label')

plt.title('Sample Bar Chart')
plt.legend()
plt.show()