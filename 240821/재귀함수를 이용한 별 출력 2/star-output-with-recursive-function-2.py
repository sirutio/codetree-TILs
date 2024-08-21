def star(N):
    if N == 0:
        return
    print('* '*N)
    star(N-1)
    print('* '*N)

N = int(input())
star(N)