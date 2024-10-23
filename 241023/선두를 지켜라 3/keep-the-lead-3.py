# 입력 처리
N, M = map(int, input().split())

# A의 이동 정보
A_moves = [tuple(map(int, input().split())) for _ in range(N)]

# B의 이동 정보
B_moves = [tuple(map(int, input().split())) for _ in range(M)]

# 총 시간 동안 A와 B의 위치를 기록할 리스트
A_positions = []
B_positions = []

# A의 위치를 기록
current_position = 0
for v, t in A_moves:
    for _ in range(t):
        current_position += v
        A_positions.append(current_position)

# B의 위치를 기록
current_position = 0
for v, t in B_moves:
    for _ in range(t):
        current_position += v
        B_positions.append(current_position)

# 명예의 전당에 올라간 사람의 조합이 바뀌는 횟수 계산
last_leader = None
changes = 0

for i in range(len(A_positions)):
    if A_positions[i] > B_positions[i]:
        leader = 'A'
    elif A_positions[i] < B_positions[i]:
        leader = 'B'
    else:
        leader = 'Tie'
    
    if leader != last_leader:
        changes += 1
        last_leader = leader

print(changes)