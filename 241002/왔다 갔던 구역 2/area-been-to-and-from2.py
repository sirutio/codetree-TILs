n = int(input())
arr = [0 for _ in range(2002)] 
loc = 1001

for _ in range(n):
    x, LorR = input().split()
    if LorR == 'L':
        for _ in range(int(x)):
            arr[loc-1] += 1
            loc -= 1
    else:
        for _ in range(int(x)):
            arr[loc+1] += 1
            loc += 1
ans = 0
for space in arr:
    if space >= 2:
        ans += 1
print(ans)