#pie charts
import matplotlib.pyplot as plt

slices=[8,2,10,4]
activities=['sleeping','eating','working','travel']
c=['c','m','r','b']
plt.pie(slices, labels=activities,colors=c,startangle=90,explode=(0,0.1,0,0),autopct='%1.1f%%',shadow=True)
plt.title('Sample Bar Chart')
plt.show()

#example2
activities=['sleeping','eating','working','travel']
c=['c','m','r','b']
plt.pie(slices, labels=activities,colors=c,startangle=90,explode=(0.3,0,0,0),autopct='%1.1f%%',shadow=True)
plt.title('Sample Bar Chart')
plt.show()

#example3
activities=['sleeping','eating','working','travel']
c=['c','m','r','b']
plt.pie(slices, labels=activities,colors=c,startangle=90,explode=(0,0,0,0.2),autopct='%1.1f%%',shadow=True)
plt.title('Sample Bar Chart')
plt.show()