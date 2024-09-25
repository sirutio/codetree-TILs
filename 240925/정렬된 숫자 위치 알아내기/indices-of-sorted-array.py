N = int(input())
nums = list(map(int,input().split()))
arr = []
for idx,num in enumerate(nums):
    arr.append([idx+1,num])

arr.sort(key=lambda x:x[1])
for i in range(N):
    arr[i].append(i+1)
arr.sort(key=lambda x:x[0])
for i in range(N):
    print(arr[i][2],end=' ')