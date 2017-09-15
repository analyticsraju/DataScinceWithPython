#Distribution 
#Distributed for different activities
import matplotlib.pyplot as plt

days=[1,2,3,4,5]

sleeping=[7,8,6,11,7]
eating=[2,3,1,3,2]
working=[10,11,9,8,9]
travel=[5,2,4,3,1]

plt.plot([],[],color='c',label='Sleeping',linewidth=5)
plt.plot([],[],color='m',label='Eating',linewidth=5)
plt.plot([],[],color='b',label='Working',linewidth=5)
plt.plot([],[],color='r',label='Travel',linewidth=5)

plt.stackplot(days,sleeping,eating,working,travel,colors=['c','m','b','r'])

plt.xlabel('X-label')
plt.ylabel('Y-label')

plt.title('Sample Bar Chart')
plt.legend()
plt.show()