import re
import sys

# Augmented Matrix Print Function
def PrintAugmentedMatrix() :
    global row
    global column
    global count

    print("\n=== Augumented Matrix ===")
    for i in range(row) :
        for j in range(column) :
            print(" %d "%(list[i][j]),end='')
        print("")
    print("============")

# ERO Print Function
def PrintERO() :
    global row
    global column
    global count

    print("\n= ERO[ %d ] ="%count)
    count += 1
    for i in range(row) :
        for j in range(column) :
            print(" %d "%(list[i][j]),end='')
        print("")
    print("============")

# RREF Print Function
def PrintRREF() :
    global row
    global column
    global count

    print("\n=== RREF ===")
    for i in range(row) :
        for j in range(column) :
            print(" %d "%(list[i][j]),end='')
        print("")
    print("============")

# REF Funtion
def REF() :
    global list
    global row
    global column

    r = row - 1
    for j in range(r) :
        for k in range(j + 1,row) :
            coef = list[k][j]
            if (list[k][j] <= list[j][j]) :
                for i in range(len(list[k])) : list[k][i] *= list[j][j]
            elif (list[j][j] != 0 and list[k][j] % list[j][j] != 0) :
                for i in range(len(list[k])) : list[k][i] *= list[j][j]

            for i in range(column) :
                list[k][i] -= (coef * list[j][i])

            if (list[k][k] < 0) :
                for i in range(len(list[k])) : list[k][i] *= -1
            PrintERO()

    if (list[r][r] != 1) :
        coef = list[r][r]
        for i in range(len(list[2])) : list[2][i] = (int)(list[2][i] / coef)
        PrintERO()

# RREF Funtion
def RREF() :
    global list
    global row
    global column

    r = row - 1
    for j in range(r, 0, -1) :
        for k in range(j - 1, -1, -1) :
            coef = list[k][j]
            if (list[k][j] <= list[j][j]) :
                for i in range(len(list[k])) : list[k][i] *= list[j][j]
            elif (list[j][j] != 0 and list[k][j] % list[j][j] != 0) :
                for i in range(len(list[k])) : list[k][i] *= list[j][j]

            for i in range(column) :
                list[k][i] -= (coef * list[j][i])
            
            if (list[k][k] < 0) :
                for i in range(len(list[k])) : list[k][i] *= -1
            if (list[k][k] != 1) :
                coef = list[k][k]
                for i in range(len(list[k])) : list[k][i] = (int)(list[k][i] / coef)
            PrintERO()

# Main
while (True) :
    exitChecker = False
    list = []
    count = 0
    name = input("파일명을 입력해주세요. ==> ")
    try :
        f = open(name, "r")
    except :
        print("%s 파일이 존재하지 않습니다. 프로그램을 종료합니다."%name)
        exitChecker = True
    finally :
        if exitChecker is True :
            break

    data = f.readlines()
    row = (int)(data[0][0])
    column = (int)(data[0][2])

    for i in range(1, row + 1) : # 변수 data에 저장된 data1.txt파일안에서 개행문자를 통해 분리하여 행렬을 찾아냅니다.
        one_line = re.findall("-?\d+", data[i])
        list.append([int(val) for val in one_line])

    PrintAugmentedMatrix()

    REF()
    RREF()

    PrintRREF()

    f.close()
    checkRepeat = input("반복 여부를 확인합니다. 다시 반복하시려면 y 또는 yes를 입력해주세요.\n")
    if (checkRepeat == "y" or checkRepeat == "yes") :
        continue
    else :
        print("프로그램을 종료합니다.")
        break
