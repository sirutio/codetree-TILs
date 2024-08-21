def printf(N):
    if N == 0:
        return
    print(N,end=' ')
    printf(N-1)
    print(N,end=' ')

N = int(input())
printf(N)