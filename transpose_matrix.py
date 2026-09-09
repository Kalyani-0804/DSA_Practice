#transpose the elements of matrix
matrix=[]
for i in range(3):
    row=list(map(int,input().split()))
    matrix.append(row)
result=[[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for i in range(3):
    for j in range(3):
        result[j][i]=matrix[i][j]
for row in result:
    print(row)