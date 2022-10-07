import re

def determinant(arr, x) :
    answer = 0
    if (x == 3) : # 3x3 정사각형 행렬일 때, determinant값을 재귀 함수의 return값으로 설정합니다.
        answer = arr[0][0] * (arr[1][1] * arr[2][2] - arr[1][2] * arr[2][1]) - (arr[0][1] * (arr[1][0] * arr[2][2] - arr[1][2] * arr[2][0])) + (arr[0][2] * (arr[1][0] * arr[2][1] - arr[1][1] * arr[2][0]))
        return answer
    else : # 3x3 정사각형 행렬이 아닐 때,
        for i in range (x) :
            mini_arr = []
            for j in range(1, x) :
                row = []
                for k in range(x) :
                    if (i == k) : continue
                    row.append(arr[j][k]) # cofactor algorithm의 원리를 이용하여 row를 저장하고
                mini_arr.append(row) # 그 행렬을 mini_arr에 저장합니다.
            det = determinant(mini_arr, x - 1) # 변수 det에 determinant 재귀함수를 통해 값을 구합니다.
            if (i % 2 == 0) : # 행렬의 1번째 row의 index가 짝수면 그대로,
                answer += (arr[0][i] * det)
            else : # 행렬의 1번째 row의 index가 홀수면 -1을 곱해 answer에 저장합니다.
                answer += (-1 * arr[0][i] * det)
    return answer # 변수 answer를 리턴합니다.

f = open("Input.txt", "r")

data = f.readlines()
length = len(data)
i = 0

file = open("Output.txt", "w")

for _ in range(3) : # 변수 data에 저장된 Input.txt파일안에서 개행문자를 통해 분리하여 행렬을 찾아냅니다.
    list = []
    while (i < length) :
        one_line_str = re.findall("-?\d+", data[i])
        i += 1
        one_line = [int(val) for val in one_line_str]
        if not one_line : # 개행문자일 경우 while문을 break하여 만들어진 행렬을 통해 determinant값을 구합니다.
            break
        list.append(one_line)

    if (len(list) != len(list[0])) : # 만들어진 행렬의 row값과 column값을 비교하여 정사각행렬이 아닐경우 det를 구할 수 없습니다.
        file.writelines("Square Matrix가 성립하지 않아, determinant를 구할 수 없습니다.\n")
    else :
        det = determinant(list, len(list))
        file.writelines((str)(det) + "\n")

file.close()
f.close()
