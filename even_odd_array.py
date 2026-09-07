"""Input: [10, 15, 22, 33, 40, 51]
Output: 
Even = [10, 22, 40]
Odd = [15, 33, 51]"""
lst =list(map(int,input().split()))
even=[]
odd=[]
for num in lst:
    if num%2==0:
        even.append(num)
    else:
        odd.append(num)
print("Even:",even)
print("Odd:",odd)