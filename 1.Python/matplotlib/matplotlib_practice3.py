#Plotting multiple plots on same window - example3
import matplotlib.pyplot as plt


x=[100,200,300,400,500]
y=[10,20,30,40,50]

x1=[150,250,350,450,550]
y1=[5,25,40,15,30]

plt.plot(x,y,label='Line 1')
plt.plot(x1,y1,label='Line 2')

plt.xlabel('X-Plot Numbers')
plt.ylabel('Y-Cordinate Values')

plt.title('Title-Sample Visualization Chart')

plt.legend()

plt.show()