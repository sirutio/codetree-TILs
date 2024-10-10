N = int(input())
ans,cnt = 0,0
arr = []

for i in range(N):
    num = int(input())
    arr.append(num)
    if i != 0 and arr[i]*arr[i-1] > 0:
        cnt += 1
    else:
        cnt = 1
    ans = max(cnt,ans)

print(ans)