# 입력받기
N = int(input())  # 숫자의 개수
numbers = [int(input()) for _ in range(N)]  # N개의 숫자를 리스트로 입력받음

# 초기화
max_length = 1  # 최대 연속 부분 수열의 길이
current_length = 1  # 현재 연속 부분 수열의 길이

# 첫 번째 숫자를 기준으로 이후 숫자들과 비교
for i in range(1, N):
    # 현재 숫자와 이전 숫자의 부호가 동일한 경우
    if (numbers[i] > 0 and numbers[i-1] > 0) or (numbers[i] < 0 and numbers[i-1] < 0):
        current_length += 1  # 연속된 수열의 길이를 증가
    else:
        # 부호가 다르면 현재까지의 최대 길이를 갱신하고, 다시 1로 초기화
        max_length = max(max_length, current_length)
        current_length = 1  # 새롭게 시작되는 수열의 길이

# 마지막 수열의 길이를 한 번 더 확인
max_length = max(max_length, current_length)

# 결과 출력
print(max_length)