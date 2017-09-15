#Distribution 
#Distributed for different activities
import matplotlib.pyplot as plt

days=[1,2,3,4,5]

sleeping=[7,8,6,11,7]
eating=[2,3,1,3,2]
working=[10,11,9,8,9]
playing=[5,2,4,3,1]

plt.stackplot(days,sleeping,eating,working,playing,colors=['c','y','b','r'])

plt.xlabel('X-label')
plt.ylabel('Y-label')

plt.title('Sample Bar Chart')
plt.legend()
plt.show()