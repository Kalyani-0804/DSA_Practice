#add elements of matrix
matrix=[]
for i in range(3):
    row =list(map(int,input().split()))
    matrix.append(row)
total=0
for row in matrix:
    for elements in row:
        total=total+elements
print(total)