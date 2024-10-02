N = int(input())
arr = [[0 for _ in range(201)] for _ in range(201)]

for _ in range(N):
    x1,y1,x2,y2 = map(int, input().split())
    for y in range(y1,y2):
        for x in range(x1,x2):
            arr[y][x] += 1
width = 0
for i in range(201):
    for j in range(201):
        if arr[i][j] != 0:
            width += 1
    
print(width)