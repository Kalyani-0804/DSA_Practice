#Print reverse array
lst =list(map(int,input().split()))
start=0
end=len(lst)-1
while start<end:
    lst[start],lst[end]=lst[end],lst[start]
    start+=1
    end-=1
print(lst)