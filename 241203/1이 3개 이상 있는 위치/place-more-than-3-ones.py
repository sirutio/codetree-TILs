# 25-28
n = int(input())
ans = 0
dxs,dxy = [1,0,-1,0], [0,1,0,-1]
a = []
for _ in range(n):
    row = list(map(int,input().split()))
    a.append(row)
# 범위 체크 
def in_range(x,y):
    return (x >= 0 and x < n) and (y >= 0 and y < n)
# 전체 돌기 
for y in range(n):
    for x in range(n):
        # x,y 기준으로 인접한 1 개수세기 
        cnt = 0
        for dx,dy in zip(dxs,dxy):
            nx,ny = x+dx,y+dy
            if in_range(nx,ny) and a[ny][nx] == 1:
                cnt += 1
        if cnt >= 3:
            ans += 1

print(ans)
