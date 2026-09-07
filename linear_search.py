"""Array: [10, 20, 30, 40, 50]
Target: 30
Output: Found at index 2  """

lst =list(map(int,input().split()))
target=int(input())
for num in lst:
    if num==target:
        print("found at index:",lst.index(num))
if num!=target:
    print("not found")