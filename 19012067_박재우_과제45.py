import re

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
    for j in range(r) : # j는 r - 1만큼
        for k in range(j + 1,row) : # k는 j + 1부터 row - 1까지
            coef = list[k][j]   # 계수
            if (list[k][j] <= list[j][j]) : # matrix k행 j번째 원소가 j행 j번째 원소보다 작거나 같으면 j행 j번째 크기만큼 곱해줌
                for i in range(len(list[k])) : list[k][i] *= list[j][j]
            elif (list[j][j] != 0 and list[k][j] % list[j][j] != 0) : # matrix k행 j번째 원소가 j행 j번째 원소로 나누어지지 않을 때도 동일하게 곱해줌
                for i in range(len(list[k])) : list[k][i] *= list[j][j]

            for i in range(column) :
                list[k][i] -= (coef * list[j][i]) # ERO 적용

            if (list[k][k] < 0) :                 # 만약 matrix k행 k번째 원소가 음수라면, 양수로 바꿔줌 (항상 -를 적용하기 위해)
                for i in range(len(list[k])) : list[k][i] *= -1
            PrintERO() # ERO 출력

    if (list[r][r] != 1) : # matrix r행 r번째 원소가 1이 아니면, 그 행을 계수로 나누어줌
        coef = list[r][r]
        for i in range(len(list[2])) : list[2][i] = (int)(list[2][i] / coef)
        PrintERO()

# RREF Funtion
def RREF() :
    global list
    global row
    global column

    r = row - 1
    for j in range(r, 0, -1) : # j는 r부터 1까지
        for k in range(j - 1, -1, -1) : # k는 j - 1부터 0까지 
            coef = list[k][j]   # 계수
            if (list[k][j] <= list[j][j]) : # matrix k행 j번째 원소가 j행 j번째 원소보다 작거나 같으면 j행 j번째 크기만큼 곱해줌
                for i in range(len(list[k])) : list[k][i] *= list[j][j]
            elif (list[j][j] != 0 and list[k][j] % list[j][j] != 0) : # matrix k행 j번째 원소가 j행 j번째 원소로 나누어지지 않을 때도 동일하게 곱해줌
                for i in range(len(list[k])) : list[k][i] *= list[j][j]

            for i in range(column) : # ERO 적용
                list[k][i] -= (coef * list[j][i])
            
            if (list[k][k] < 0) : # 만약 matrix k행 k번째 원소가 음수라면, 양수로 바꿔줌 (항상 -를 적용하기 위해)
                for i in range(len(list[k])) : list[k][i] *= -1
            if (list[k][k] != 1) : # matrix k행 k번째 원소가 1이 아니면, 그 행을 계수로 나누어줌
                coef = list[k][k]  # RREF를 만들기 위해
                for i in range(len(list[k])) : list[k][i] = (int)(list[k][i] / coef)
            PrintERO()

# Main
while (True) :
    exitChecker = False # 파일이 존재하지 않는지 확인하는 Flag
    list = []
    count = 0
    name = input("파일명을 입력해주세요. ==> ")
    try : # 파일 열기
        f = open(name, "r")
    except : # 예외 처리
        print("%s 파일이 존재하지 않습니다. 프로그램을 종료합니다."%name)
        exitChecker = True
    finally :
        if exitChecker is True :
            break

    data = f.readlines()
    row = (int)(data[0][0])
    column = (int)(data[0][2])

    for i in range(1, row + 1) : # 리스트 list에 2차원 리스트로 matrix 삽입
        one_line = re.findall("-?\d+", data[i])
        list.append([int(val) for val in one_line])

    PrintAugmentedMatrix()  # Augmented Matrix Print

    REF()                   # REF Function
    RREF()                  # RREF Function

    PrintRREF()             # RREF Print

    f.close()
    checkRepeat = input("반복 여부를 확인합니다. 다시 반복하시려면 y 또는 yes를 입력해주세요.\n")
    if (checkRepeat == "y" or checkRepeat == "yes") : # y또는 yes를 입력할 경우 다시 파일명 입력 받기
        continue
    else : # 예외 처리
        print("프로그램을 종료합니다.") 
        break
