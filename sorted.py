"check the array is sorted or not"
lst=list(map(int,input().split()))
is_sorted=True
for i in range(len(lst)-1):
    if lst[i]>lst[i+1]:
        is_sorted=False
print(is_sorted)   
