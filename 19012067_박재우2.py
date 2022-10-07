import re

from numpy import real

def determinant(arr, x) :
    ans = 0
    if (x == 3) :
        answer = arr[0][0] * (arr[1][1] * arr[2][2] - arr[1][2] * arr[2][1]) - (arr[0][1] * (arr[1][0] * arr[2][2] - arr[1][2] * arr[2][0])) + (arr[0][2] * (arr[1][0] * arr[2][1] - arr[1][1] * arr[2][0]))
        return answer
    else :
        for i in range (x) :
            mini_arr = []
            for j in range(1, x) :
                row = []
                for k in range(x) :
                    if (i == k) : continue
                    row.append(arr[j][k])
                mini_arr.append(row)
            team = determinant(mini_arr, x - 1)
            if (i % 2 == 0) :
                ans += (arr[0][i] * team)
            elif (i % 2 == 1) :
                ans += (-1 * arr[0][i] * team)
    return ans

f = open("Input.txt", "r")

list = []
data = f.readlines()
length = len(data)
count = 0
real_answer = 0

for i in range(length) :
    one_line_str = re.findall("-?\d+", data[i])
    one_line = [int(i) for i in one_line_str]
    list.append(one_line)

count = len(one_line)

if (count != length) :
    print("Square Matrix가 성립하지 않아, determinant를 구할 수 없습니다.")
    exit()

real_answer = determinant(list, count)

print(real_answer)

# 0 0 2 0
# 1 2 17 -3
# -1 0 28 1
# -2 2 -37 1

# 2 -4 3
# 3 1 2
# 1 4 -1

# 1 1 1 2 1
# 1 2 2 1 1
# 1 3 3 0 1
# 1 2 2 2 2
# 1 1 1 1 1

#for i in range((int)(data[1][2])) :
#    one_line = re.findall("-?\d+", data[i + 2])
#    list.append(one_line)

#for i in range((int)(data[(int)(data[1][2]) + 3][2])) :
#    one_line = re.findall("-?\d+", data[i + (int)(data[1][2]) + 4])
#    list.append(one_line)

#file = open("Output.txt", "w")

#if (data[1][2] != data[(int)(data[1][2]) + 3][2] or\
#    data[1][4] != data[(int)(data[1][2]) + 3][4]) :
#    file.writelines("+ 계산 불가")

#else :
#    answer = []
#    for i in range((int)(data[1][2])) :
#        one_answer = []
#        for j in range((int)(data[1][4])) :
##            one_answer.append((int)(list[i][j]) + (int)(list[i + (int)(data[1][2])][j]))
#        answer.append(one_answer)
#        answer.append('\n')
    
#    for lines in answer :
#        result = ' '.join(str(i) for i in lines)
#        file.writelines(result)

#file.close()
f.close()
