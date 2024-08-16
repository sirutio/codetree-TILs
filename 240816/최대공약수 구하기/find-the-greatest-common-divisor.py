def CommonDivisor(n,m):
    if n >= m:
        for i in range(m,1,-1):
            if n%i == 0 and m%i == 0:
                print(i)
                break
    else:
        for i in range(n,1,-1):
            if m%i == 0 and n%i == 0:
                print(i)
                break
    

n, m = map(int,input().split())
CommonDivisor(n,m)