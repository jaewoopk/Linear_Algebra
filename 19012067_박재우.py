import re

f = open("Input01.txt", "r")

data = f.readlines()

print(data)
for i in range((int)(data[1][2])) :
    list = re.findall("-?\d+", data[i + 2])
    print(list)

for i in range((int)(data[6][2])) :
    list = re.findall("-?\d+", data[i + 7])
    print(list)

f.close
