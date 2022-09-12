import re

f = open("Input01.txt", "r")

data = f.readlines()

list = []
for i in range((int)(data[1][2])) :
    one_line = re.findall("-?\d+", data[i + 2])
    list.append(one_line)

for i in range((int)(data[(int)(data[1][2]) + 3][2])) :
    one_line = re.findall("-?\d+", data[i + (int)(data[1][2]) + 4])
    list.append(one_line)

print(list)
f.close
