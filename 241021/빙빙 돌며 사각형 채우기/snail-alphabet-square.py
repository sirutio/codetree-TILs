n, m = map(int, input().split())  # n: 행(row), m: 열(column)

# n * m 크기의 직사각형을 담을 리스트 초기화
grid = [[''] * m for _ in range(n)]

# 방향 설정 (오른쪽, 아래쪽, 왼쪽, 위쪽)
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
x, y, d = 0, 0, 0  # 시작 위치 및 방향 (x: 행, y: 열, d: 방향 인덱스)
current_char = 0  # 현재 알파벳 인덱스 (A부터 시작)

for i in range(n * m):
    grid[x][y] = chr(current_char + ord('A'))  # 현재 위치에 알파벳 채우기
    current_char = (current_char + 1) % 26  # Z 다음에는 다시 A부터 시작
    
    # 다음 위치 계산
    nx, ny = x + directions[d][0], y + directions[d][1]
    
    # 직사각형 범위를 벗어나거나 이미 채워진 곳이면 방향 전환
    if not (0 <= nx < n and 0 <= ny < m and grid[nx][ny] == ''):
        d = (d + 1) % 4  # 방향 전환
        nx, ny = x + directions[d][0], y + directions[d][1]
    
    x, y = nx, ny  # 새로운 위치로 이동

# 결과 출력
for row in grid:
    print(' '.join(row))