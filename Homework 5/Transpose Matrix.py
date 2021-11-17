matrix = [[1,2,3],[4,5,6],[7,8,9]]
lenn = len(matrix)
transpose = []
for i in range(lenn):
    transpose.append([])
    for j in range(lenn):
        transpose[i].append(matrix[j][i])
print(matrix)
print(transpose)        




