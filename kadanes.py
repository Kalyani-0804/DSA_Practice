#Kadane's Algorithm (Maximum Subarray Sum):
lst=list(map(int,input().split()))
current_sum=lst[0]
max_sum=lst[0]
for i in range(1,len(lst)):
    num=lst[i]
    current_sum=max(num,current_sum+num)
    if current_sum>max_sum:
        max_sum=current_sum
print(max_sum)