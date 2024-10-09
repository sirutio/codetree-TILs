OFFSET = 1000
arr = [[0 for _ in range(OFFSET*2+1)] for _ in range(OFFSET*2+1)]

x1,y1,x2,y2 = map(int,input().split())
x1,y1,x2,y2 = x1+OFFSET,y1+OFFSET,x2+OFFSET,y2+OFFSET
for i in range(y1,y2):
    for j in range(x1,x2):
        arr[i][j] = 1

x3,y3,x4,y4 = map(int,input().split())
x3,y3,x4,y4 = x3+OFFSET,y3+OFFSET,x4+OFFSET,y4+OFFSET
for i in range(y3,y4):
    for j in range(x3,x4):
        arr[i][j] = 2
    
min_x,max_x = OFFSET*2+1,-1
min_y,max_y = OFFSET*2+1,-1
for i in range(y1,y2):
    for j in range(x1,x2):
        if arr[i][j] == 1:
            if j > max_x:
                max_x = j
            if j < min_x:
                min_x = j
        if i > max_y:
            max_y = i
        if i < min_y:
            min_y = i

print((max_x-min_x+1)*(max_y-min_y+1))