row = int(input())
col = int(input())
mat = [[int(input()) for x in range(col)] for y in range(row)]

for i in range(row):
    for j in range(0, i):
        mat[i][j] , mat[j][i] = mat[j][i], mat[i][j]

for i in range(row):
    for j in range(col):
        print(mat[i][j], end =" ")
    print()

