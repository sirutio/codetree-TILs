def snail(n, m):
    arr = [[0] * m for _ in range(n)]
    dx = [0, 1, 0, -1]  # 오른쪽, 아래, 왼쪽, 위쪽 순서
    dy = [1, 0, -1, 0]
    
    x, y, direction = 0, 0, 0  # 시작 위치 및 방향 설정
    for num in range(1, n * m + 1):
        arr[x][y] = num
        nx, ny = x + dx[direction], y + dy[direction]
        
        if nx < 0 or nx >= n or ny < 0 or ny >= m or arr[nx][ny] != 0:
            direction = (direction + 1) % 4  # 방향 전환
            nx, ny = x + dx[direction], y + dy[direction]
        
        x, y = nx, ny
    
    for row in arr:
        print(' '.join(map(str, row)))

# 입력
n, m = map(int, input().split())
snail(n, m)