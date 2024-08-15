def rectangle(n,m):
    for _ in range(n):
        for _ in range(m):
            print('1',end='')
        print()

n,m = tuple(map(int,input().split()))
rectangle(n,m)