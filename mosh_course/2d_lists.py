matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

matrix[0][1] = 123
print(matrix[1][1])

for x in matrix:
    for item in x:
        print(item)