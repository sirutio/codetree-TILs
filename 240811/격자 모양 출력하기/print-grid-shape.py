n,m  = list(map(int,input().split()))
arr = [[0 for _ in range(n)] for _ in range(n)]

for _ in range(m):
    r,c = tuple(map(int,input().split()))
    arr[r-1][c-1] = r*c

for i in range(n):
    for j in range(n):
        print(arr[i][j], end=' ')
    print()