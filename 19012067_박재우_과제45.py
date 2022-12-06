import re

list = []

def ERO() :
    global list

    for j in range(1,3) :
        for k in range(j + 1,3) :
            if (list[k][j] % list[j][j] != 0) :
                for i in range(len(list[k])) : list[k][i] *= list[0][0]

            coef = list[k][j]

            for i in range(4) :
                list[k][i] -= (coef * list[j][i])

    # if (list[2][0] % list[0][0] != 0) :
    #     for i in range(len(list[2])) : list[2][i] *= list[0][0]

    # coef = list[2][0]

    # for i in range(4) :
    #     list[2][i] -= (coef * list[0][i])

    # if (list[2][1] % list[1][1] != 0) :
    #     for i in range(len(list[2])) : list[2][i] *= list[1][1]

    # coef = list[2][1]

    # for i in range(4) :
    #     list[2][i] -= (coef * list[1][i])
    
    if (list[2][2] != 1) :
        coef = list[2][2]
        for i in range(len(list[2])) : list[2][i] = (int)(list[2][i] / coef)


f = open("data1.txt", "r")

data = f.readlines()
length = len(data)

file = open("Output.txt", "w")

for i in range(length) : # 변수 data에 저장된 data1.txt파일안에서 개행문자를 통해 분리하여 행렬을 찾아냅니다.
    one_line = re.findall("-?\d+", data[i])
    list.append([int(val) for val in one_line])

print(list)

ERO()

print(list)

file.close()
f.close()
