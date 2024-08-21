def sum_p(N):
    if N == 1:
        return 1
    return sum_p(N-1) + N

N = int(input())
print(sum_p(N))