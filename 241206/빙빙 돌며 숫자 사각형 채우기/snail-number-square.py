n,m = map(int,input().split())
arr = [[0 for _ in range(m)] for _ in range(n)]

def in_range(x,y):
    return x >= 0 and x < n and y >= 0 and y < m

x,y = 0,0
dir_num = 0
dy,dx = [1,0,-1,0],[0,1,0,-1]

arr[x][y] = 1
for i in range(2,n*m+1):
    nx,ny = x+dx[dir_num], y+dy[dir_num]
    if not in_range(nx,ny) or (arr[nx][ny] != 0):
        dir_num = (dir_num+1)%4
    x,y = x+dx[dir_num], y+dy[dir_num]
    arr[x][y] = i

# 결과 출력 
for i in range(n):
    for j in range(m):
        print(arr[i][j], end=' ')
    print()
