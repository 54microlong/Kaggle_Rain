import sys


inp = open('mean_Deri_train_wl', 'r')
res = []
for line in inp:
   res.append(line.strip().split(' '))

# get element 2,3
print(res[2][3])

# get row 2
print(res[2])

# get column 5
column = []
for i in range(len(res)):
    column.append(res[i][5])

print(column)
