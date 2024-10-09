N = int(input())
OFFSET = 100
arr = [[0 for _ in range(OFFSET*2+1)] for _ in range(OFFSET*2+1)]

for _ in range(N):
    x,y = map(int,input().split())
    x,y = x+OFFSET, y+OFFSET
    for i in range(y,y+8):
        for j in range(x,x+8):
            arr[i][j] = 1
        
ans = 0
for row in arr:
    for col in row:
        if col == 1:
            ans += 1
print(ans)