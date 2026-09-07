"""Input: [10, 45, 3, 67, 22]
Output: 2nd Largest = 45"""

lst = list(map(int,input().split()))
largest_num =lst[0]
sec_largest=lst[0]
for num in lst:
    if largest_num <num:
        sec_largest=largest_num
        largest_num=num
        
print(sec_largest)
print(largest_num)
        