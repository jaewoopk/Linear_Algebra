import pandas as pd

df = pd.read_table("Input01.txt")
print(df)
f = open("Input01.txt", "r")

n = (int)(f.readline().strip())


for _ in range(n) :
    list = []
    line = f.readline()
    for i in range((int)(line[2])) :
        row = f.readline()
        one_row = []
        for j in range((int)(line[4])) :
            one_row.append((row[2 * j]))
        list.append(one_row)
    line = f.readline()
#lines = f.readlines()

#for line in lines :
#    a = 1


f.close