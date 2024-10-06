def max_length_subsequence(n, t, sequence):
    max_length = 0
    current_length = 0

    for num in sequence:
        if num > t:
            current_length += 1
            max_length = max(max_length, current_length)
        else:
            current_length = 0

    return max_length

# 입력 받기
n, t = map(int, input().split())
sequence = list(map(int, input().split()))

# 결과 출력
print(max_length_subsequence(n, t, sequence))