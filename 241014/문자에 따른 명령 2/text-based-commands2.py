# 방향은 북(0), 동(1), 남(2), 서(3)로 설정
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 북, 동, 남, 서

def final_position(commands):
    x, y = 0, 0  # 시작 좌표
    direction = 0  # 처음에 북쪽(0)을 바라보고 있음

    for command in commands:
        if command == 'L':  # 왼쪽으로 회전하면 방향을 90도 반시계방향(방향 -1)
            direction = (direction - 1) % 4
        elif command == 'R':  # 오른쪽으로 회전하면 방향을 90도 시계방향(방향 +1)
            direction = (direction + 1) % 4
        elif command == 'F':  # 한 칸 전진
            dx, dy = directions[direction]
            x += dx
            y += dy

    return x, y

# 입력 받기
commands = input().strip()

# 결과 출력
x, y = final_position(commands)
print(x, y)