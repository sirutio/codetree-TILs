def square(N):
    cnt = 1
    for _ in range(N):
        for _ in range(N):
            if cnt >= 10:
                cnt = 1
            print(cnt, end=' ')
            cnt += 1
        print()

N = int(input())
square(N)