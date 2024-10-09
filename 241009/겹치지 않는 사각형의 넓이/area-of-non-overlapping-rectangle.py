OFFSET = 1000
arr = [[0 for _ in range(OFFSET*2+1)] for _ in range(OFFSET*2+1)]

for _ in range(2):
    x1,y1,x2,y2 = map(int,input().split())
    x1,y1,x2,y2 = x1+OFFSET, y1+OFFSET, x2+OFFSET, y2+OFFSET
    for i in range(y1,y2):
        for j in range(x1,x2):
            arr[i][j] = 1
x1,y1,x2,y2 = map(int,input().split())
x1,y1,x2,y2 = x1+OFFSET, y1+OFFSET, x2+OFFSET, y2+OFFSET
for i in range(y1,y2):
        for j in range(x1,x2):
            arr[i][j] = 0

ans = 0
for row in arr:
    for col in row:
        if col == 1:
            ans += 1
    
print(ans)