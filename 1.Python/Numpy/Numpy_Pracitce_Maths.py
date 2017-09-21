

height=[1,2,3.2,2.1,4.5]
weight=[45,40,45,25,25]

BMI=height[0]*weight[0]
BMI=height*weight#failed in lists, but this will work with numpy
BMI=height+weight
BMI=height/weight#failed in lists, but this will work with numpy


#beauty of arrays(numpy) as below as compared to lists
import numpy as np

h=np.array(height)
w=np.array(weight)

bmi=h*w
bmi=h+w
bmi=h/w
