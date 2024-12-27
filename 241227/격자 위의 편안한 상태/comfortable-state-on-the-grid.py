N,M = map(int,input().split())
arr = [[0 for _ in range(N)] for _ in range(N)]

def in_range(r,c):
    if r < N and c < N and r > -1 and c > -1:
        return True
    else:
        return False 

def check(r,c):
    dx,dy = [1,0,-1,0],[0,-1,0,1]
    cnt = 0
    for x,y in zip(dx,dy):
        nx,ny = c+x, r+y
        if in_range(nx,ny) and arr[ny][nx] == 1:
            cnt += 1 
    if cnt == 3:
        return True
    else:
        return False


for i in range(M):
    r,c = map(int,input().split())
    arr[r-1][c-1] = 1
    print(int(check(r-1,c-1))) # 열(가로)과 행(세로)