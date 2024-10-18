def back_to_origin(N, movements):
    # 현재 위치를 (0, 0)에서 시작
    x, y = 0, 0
    total_time = 0
    
    # 각 방향에 따른 이동량을 설정
    direction_map = {'N': (0, 1), 'S': (0, -1), 'E': (1, 0), 'W': (-1, 0)}
    
    # 움직임 처리
    for direction, distance in movements:
        dx, dy = direction_map[direction]
        
        # 거리만큼 이동
        for _ in range(distance):
            x += dx
            y += dy
            total_time += 1
            
            # 처음으로 (0, 0)에 돌아오면 시간을 출력
            if x == 0 and y == 0:
                return total_time
    
    # 모든 이동을 마쳤는데도 돌아오지 못하면 -1 출력
    return -1

# 입력 처리
N = int(input())
movements = [input().split() for _ in range(N)]
movements = [(direction, int(distance)) for direction, distance in movements]

# 결과 출력
print(back_to_origin(N, movements))