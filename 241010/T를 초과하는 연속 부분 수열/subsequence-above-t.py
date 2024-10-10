n,t = map(int,input().split())
arr = list(map(int,input().split()))
ans, cnt = 0,0

for i,num in enumerate(arr):
    if i != 0 and num > t:
        cnt += 1
    elif num > t:
        cnt = 1
    else:
        cnt = 0
    ans = max(ans,cnt)

print(ans)