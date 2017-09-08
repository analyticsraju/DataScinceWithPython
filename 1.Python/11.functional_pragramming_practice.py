#Example1
age = [10,20,30,40,50]
i=0
for age1 in age:
    age[i]=age1+10;
    i=i+1
print(age)

#Example2
age = [10,20,30,40,50]
i=0
for i,age1 in enumerate(age):
    age[i]=age1+10;
print(age)


#Example3
age = [10,20,30,40,50]
def incr(e):
    return e+10;
age=map(incr,age)
age=list(age)#converting map to list
print(age)

#Example4
age=map(lambda e:e+10,age)#in java anonymous class create and use of it method then and there and leave it.
age=list(age) #here lamba function also does same, implement incrementation take care automatically[map(lamba e:e+10, age)]
print(age) #this short way usage for loops and incrementing columns
