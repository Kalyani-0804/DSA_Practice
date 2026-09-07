"""Array: [2, 7, 11, 15]
Target: 9
Output: 2 and 7 (indices 0 and 1)"""
lst=list(map(int,input().split()))
target=int(input())
for i in range(len(lst)):
    for j in range(i+1,len(lst)):
        if lst[i]+lst[j]==target:
            print(lst[i],lst[j],"indices",i,"and",j)