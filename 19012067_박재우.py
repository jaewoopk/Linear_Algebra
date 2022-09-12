import re

f = open("Input02.txt", "r")

data = f.readlines()

list = []
for i in range((int)(data[1][2])) :
    one_line = re.findall("-?\d+", data[i + 2])
    list.append(one_line)

for i in range((int)(data[(int)(data[1][2]) + 3][2])) :
    one_line = re.findall("-?\d+", data[i + (int)(data[1][2]) + 4])
    list.append(one_line)

file = open("Output02.txt", "w")

if (data[1][2] != data[(int)(data[1][2]) + 3][2] or\
    data[1][4] != data[(int)(data[1][2]) + 3][4]) :
    file.writelines("+ 계산 불가")

else :
    answer = []
    for i in range((int)(data[1][2])) :
        one_answer = []
        for j in range((int)(data[1][4])) :
            one_answer.append((int)(list[i][j]) + (int)(list[i + (int)(data[1][2])][j]))
        answer.append(one_answer)
        answer.append('\n')
    
    for lines in answer :
        result = ' '.join(str(i) for i in lines)
        file.writelines(result)

file.close()
f.close()
