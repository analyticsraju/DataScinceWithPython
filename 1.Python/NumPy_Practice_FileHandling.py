#File reading
import os

os.getcwd
os.chdir('D:/Data/DataScience/Practice/DSWithPython/')



fd=open('raju.txt','r')

for line in fd:
    print(line)
#fd.close()

fd.tell()

fd.seek(6)
a = fd.read(10)

fd.seek(0,0)#start
fd.seek(2)
a = fd.read()

fd.seek(0)
a=fd.tell()
test=fd.seek(5,0)
fd.read()

fd.seek(0,0)#start
a=fd.tell()
t=fd.seek(10,0)


test=fd.seek(0,2)
a=fd.tell()

test=fd.seek(1,2)
a=fd.tell()

    


