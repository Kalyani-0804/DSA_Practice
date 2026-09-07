"""Input: [1, 2, 3, 4, 5], k = 2
Output: [3, 4, 5, 1, 2]"""

lst =list(map(int,input().split()))
k=int(input())
new_list=[]
for i in range(k,len(lst)):
    new_list.append(lst[i])
for j in range(0,k):
    new_list.append(lst[j])
print(new_list)