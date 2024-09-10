N = int(input())
arr = list(map(int,input().split()))
arr.sort()
val = 0
for i in range(N):
    temp = arr[i]+arr[2*N-i-1]
    if temp > val:
        val = temp

print(val)