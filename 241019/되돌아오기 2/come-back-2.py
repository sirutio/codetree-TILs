def back_to_origin(commands):
    # 초기 위치와 방향
    x, y = 0, 0
    direction = 0  # 북쪽을 0, 동쪽을 1, 남쪽을 2, 서쪽을 3으로 설정
    
    # 북, 동, 남, 서에 따른 좌표 변화량
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    # 총 시간을 저장할 변수
    total_time = 0
    
    # 명령 처리
    for command in commands:
        total_time += 1
        
        if command == 'L':
            # 왼쪽으로 회전 (90도 반시계 방향)
            direction = (direction - 1) % 4
        elif command == 'R':
            # 오른쪽으로 회전 (90도 시계 방향)
            direction = (direction + 1) % 4
        elif command == 'F':
            # 현재 방향으로 한 칸 이동
            dx, dy = directions[direction]
            x += dx
            y += dy
        
        # 처음으로 (0, 0)에 돌아오면 시간을 반환
        if x == 0 and y == 0:
            return total_time
    
    # 끝까지 돌아오지 못했다면 -1 반환
    return -1

# 입력 처리
commands = input().strip()

# 결과 출력
print(back_to_origin(commands))