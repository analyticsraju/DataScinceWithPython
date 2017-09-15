#Sample plot of Bar style example-4
import matplotlib.pyplot as plt

x=[10,20,30,40,50]
y=[15,10,20,25,30]

x1=[5,15,25,35,45]
y1=[10,5,7,15,20]

plt.bar(x,y,label='Bar Styple-1',color='r')
plt.bar(x1,y1,label='Bar Styple-2',color='c')

plt.xlabel('X-label')
plt.ylabel('Y-label')

plt.title('Sample Bar Chart')
plt.legend()
plt.show()