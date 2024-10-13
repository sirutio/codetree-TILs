# 입력 받기
N = int(input())  # 움직이는 횟수
x, y = 0, 0  # 초기 위치 (0, 0)

# 방향에 따른 dx, dy 값 설정
direction_map = {
    'N': (0, 1),  # 북쪽으로 이동하면 y가 증가
    'S': (0, -1), # 남쪽으로 이동하면 y가 감소
    'E': (1, 0),  # 동쪽으로 이동하면 x가 증가
    'W': (-1, 0)  # 서쪽으로 이동하면 x가 감소
}

# N번의 움직임 처리
for _ in range(N):
    direction, distance = input().split()
    distance = int(distance)
    
    # 해당 방향에 맞게 dx, dy 값을 얻어서 위치 갱신
    dx, dy = direction_map[direction]
    x += dx * distance
    y += dy * distance

# 최종 위치 출력
print(x, y)