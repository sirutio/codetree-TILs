n,m = map(int,input().split())
arr = [[0 for _ in range(m)] for _ in range(n)]

def in_range(x,y):
    return x >= 0 and x < n and y >= 0 and y < m

x,y = 0,0
dir_num = 0
dy,dx = [1,0,-1,0],[0,1,0,-1]

# 돌면서 범위 안에 있고 이미 숫자가 적혀 있는 게 아니라면 업데이트
# x,y가 n행 m열로, 가로가 배열에서는 세로(첫 번째 인덱스)가 된다는 점을 인지하기  
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
