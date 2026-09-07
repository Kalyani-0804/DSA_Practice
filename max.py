"""Input: [10, 45, 3, 67, 22]
Output: Maximum = 67"""

lst = list(map(int,input().split()))
max=lst[0]
for num in lst:
    if num>max:
        max=num
print(max)