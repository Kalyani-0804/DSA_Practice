"""Input: [10, 45, 3, 67, 22]
Output: 64   ( 67 - 3 = 64)"""

lst = list(map(int,input().split()))
max_num=lst[0]
min_num=lst[0]
for num in lst:
    if num>max_num:
        max_num=num
    if num<min_num:
        min_num=num
print(max_num)
print(min_num)
diff=max_num-min_num
print(diff)