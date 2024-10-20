# N: 격자의 크기, M: 색칠하는 횟수
N, M = map(int, input().split())

# N x N 격자를 0으로 초기화 (0은 아직 색칠되지 않은 상태)
grid = [[0] * N for _ in range(N)]

# 상하좌우 이동을 위한 방향 설정
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# 각 색칠에 대해 '편안한 상태'인지 확인하는 함수
def is_comfortable(r, c):
    adjacent_count = 0
    
    # 네 방향의 인접한 칸을 확인
    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if 0 <= nr < N and 0 <= nc < N:  # 격자 내에 있는 칸만 고려
            if grid[nr][nc] == 1:        # 인접 칸이 색칠되어 있으면
                adjacent_count += 1
    
    # 인접 칸 중 정확히 3개가 색칠되어 있으면 편안한 상태
    return adjacent_count == 3

# M번에 걸쳐 색칠할 칸의 위치를 입력받음
for _ in range(M):
    r, c = map(int, input().split())
    r -= 1  # 0-based index로 변환
    c -= 1  # 0-based index로 변환
    
    # 해당 칸에 색칠
    grid[r][c] = 1
    
    # 해당 칸이 편안한 상태인지 확인하고 출력
    if is_comfortable(r, c):
        print(1)
    else:
        print(0)