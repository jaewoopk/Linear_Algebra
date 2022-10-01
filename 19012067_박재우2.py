import re

def determinant(arr, x) :
    if (x == 0) :
        return arr[0][x] * (arr[1][1] * arr[2][2] - arr[1][2] * arr[2][1])
    elif (x == 1) :
        return arr[0][x] * (arr[1][0] * arr[2][2] - arr[1][2] * arr[2][0])
    elif (x == 2) :
        return arr[0][x] * (arr[1][0] * arr[2][1] - arr[1][1] * arr[2][0])


f = open("Input.txt", "r")

list = []
data = f.readlines()
length = len(data)
count = 0
ans = 0

for i in range(length) :
    one_line_str = re.findall("-?\d+", data[i])
    one_line = [int(i) for i in one_line_str]
    list.append(one_line)

count = len(one_line)

if (count != length) :
    print("Square Matrix가 성립하지 않아, determinant를 구할 수 없습니다.")
    exit()

for i in range(count) :
    if (i % 2 == 0) :
        ans += determinant(list, i)
    else :
        ans += (-1 * determinant(list, i))
        
print(ans)

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
