n = int(input())  # 집의 개수
A = list(map(int, input().split()))  # 각 집에 사는 사람 수

# 최소 이동 거리 합을 저장할 변수
min_distance = float('inf')

# 각 집을 모임 장소로 가정
for meeting_point in range(n):
    total_distance = 0
    for i in range(n):
        total_distance += abs(meeting_point - i) * A[i]  # 각 집과의 거리 * 사람 수
    # 최소 이동 거리 합을 갱신
    min_distance = min(min_distance, total_distance)

print(min_distance)