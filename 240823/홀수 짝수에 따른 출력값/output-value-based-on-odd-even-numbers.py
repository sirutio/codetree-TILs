def printf(N):
    if N < 1:
        return 0

    if N%2 != 0:
        return printf(N-2) + N
    else:
        return printf(N-2) + N

N = int(input())
print(printf(N))