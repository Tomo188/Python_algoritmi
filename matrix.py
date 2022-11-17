x = [[1, 2], [2, 3]]
y = [[2, 3], [3, 4]]
result = [[0, 0], [0, 0]]
'''
for i in range(len(x)):
    for j in range(len(y[0])):
        for k in range(len(y)):
            result[i][j] += x[i][k]*y[k][j]
'''

for i in range(2):
    for j in range(2):
        result[i][j] += x[i][j]*y[i][j]
print(result)
