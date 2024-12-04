n,m = map(int,input().split())
arr = [[0 for _ in range(m)] for _ in range(n)]
x,y = 0,0
dir_num = 0
dx,dy = [1,0,-1,0],[0,-1,0,1]

def in_range(x,y):
    return x >= 0 and x < m and y >= 0 and y < n

for i in range(1,n*m+1):
    nx,ny = x+dx[dir_num], y+dy[dir_num]
    if not in_range(nx,ny) or (arr[ny][nx] != 0):
        dir_num = (dir_num+1)%4
    x,y = x+dx[dir_num], y+dy[dir_num]
    arr[dir_num] = i
'''
# 결과 출력 
for i in range(n):
    for j in range(m):
        print(arr[i][j], end=' ')
    print()
'''