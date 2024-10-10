n,t = map(int,input().split())
arr = list(map(int,input().split()))
ans, cnt = 0,0

for num in arr:
    if num > t:
        cnt += 1
    else:
        cnt = 0
    ans = max(ans,cnt)

print(ans)