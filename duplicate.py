"""Input: [10, 20, 30, 20, 40, 10]
Output: Duplicates = [20, 10]"""

lst=list(map(int,input().split()))
count ={}
for num in lst:
    if num in count:
        count[num]+=1
    else:
        count[num]=1
for key, value in count.items():
    if value > 1:
        print(key)