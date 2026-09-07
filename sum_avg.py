"""Input: [10, 20, 30, 40]
Output: Sum = 100, Average = 25.0"""
lst =list(map(int,input().split()))
total=0
for num in lst:
    total = total+num
avg = total/len(lst)
print(total)
print(avg)