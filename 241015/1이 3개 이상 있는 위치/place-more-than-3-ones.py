# 입력 받기
n = int(input())  # 격자의 크기 n
grid = [list(map(int, input().split())) for _ in range(n)]  # n * n 격자 입력 받기

# 상하좌우 이동을 위한 방향 벡터 (row, col)
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# 인접한 1의 개수가 3개 이상인 칸의 개수를 저장할 변수
count = 0

# 각 칸을 순회하면서 인접한 칸에 1이 몇 개 있는지 확인
for i in range(n):
    for j in range(n):
        adjacent_ones = 0  # 인접한 1의 개수
        
        # 상하좌우 확인
        for dr, dc in directions:
            ni, nj = i + dr, j + dc
            # 인접한 칸이 격자 범위 안에 있고, 그 칸이 1인 경우 개수를 증가시킴
            if 0 <= ni < n and 0 <= nj < n and grid[ni][nj] == 1:
                adjacent_ones += 1
        
        # 인접한 칸에 1이 3개 이상인 경우 count 증가
        if adjacent_ones >= 3:
            count += 1

# 결과 출력
print(count)