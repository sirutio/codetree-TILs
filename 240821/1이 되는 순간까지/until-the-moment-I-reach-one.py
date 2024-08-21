def count(N):
    if N == 1:
        return 0
    if N%2 == 0:
        return count(N//2) + 1
    else:
        return count(N//3) + 1

N = int(input())
print(count(N))