import os

f = open((os.path.dirname(__file__) + '\\file.txt'), 'r')
temp = ""
while(f.readline() != ""):
    temp += f.readline()
f.close()

print(temp)