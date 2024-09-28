a,b,c, = map(int,input().split())
if a<11 or (a==11 and b<11) or (a==11 and b==11 and c<11):
    print(-1)
else:
    ans = (a-11)*60*24+(b-11)*60+(c-11)
    print(ans)