#print minimum number in array
lst = list(map(int,input().split()))
minimum =lst[0]
for num in lst:
    if num <minimum:
        minimum=num
print(minimum) 