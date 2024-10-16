def move_ball(n, t, r, c, d):
    # 방향에 따른 row, col 변화량
    dir_map = {
        'U': (-1, 0),  # 위로
        'D': (1, 0),   # 아래로
        'L': (0, -1),  # 왼쪽으로
        'R': (0, 1)    # 오른쪽으로
    }

    # 반대 방향으로 변경하는 맵
    reverse_dir = {
        'U': 'D',
        'D': 'U',
        'L': 'R',
        'R': 'L'
    }

    # 현재 위치와 방향
    row, col = r, c
    direction = d

    for _ in range(t):
        dr, dc = dir_map[direction]
        new_row, new_col = row + dr, col + dc

        # 벽에 부딪히는지 확인
        if new_row < 1 or new_row > n or new_col < 1 or new_col > n:
            # 방향을 반대로 바꾸고 이동하지 않음
            direction = reverse_dir[direction]
            continue  # 이 시간 동안 이동하지 않음
        else:
            # 이동 가능하면 위치 업데이트
            row, col = new_row, new_col

    return row, col

# 입력 받기
n, t = map(int, input().split())
r, c, d = input().split()
r, c = int(r), int(c)

# 결과 계산
result_row, result_col = move_ball(n, t, r, c, d)

# 결과 출력
print(result_row, result_col)