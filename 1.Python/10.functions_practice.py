#Functions basics

#creating orbitary function
def add(a,b,c):
    temp=a+b;
    temp=temp+c
    return temp

output = add(10,20,30)
print(output)

#creating another orbitary function
def add2(a,b=5,c=10):
    temp=a+b
    temp=temp+c
    return temp

#below fucntion applies a=10,b=5,c=10
output2 = add2(10)
print(output2)

#below works like a=10,b=5,c=20
output3 = add2(10,c=20)
print(output3)