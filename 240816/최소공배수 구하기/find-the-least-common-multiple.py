def CommonMultiple(n,m):
    ans = max(n,m)
    cnt = 1
    while 1:
        ans = max(n,m)*cnt
        if ans%n == 0 and ans%m == 0:
            print(ans)
            break
        cnt += 1
    

n,m = map(int,input().split())
CommonMultiple(n,m)