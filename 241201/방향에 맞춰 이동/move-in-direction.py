N = int(input())
x,y = 0,0
dx,dy = [1,-1,0,0],[0,0,-1,1]

for _ in range(N):
    way,dis = input().split()
    if way == 'W':
        x,y = x+dx[1]*int(dis),y+dy[1]*int(dis)
    elif way == 'S':
        x,y = x+dx[2]*int(dis),y+dy[2]*int(dis)
    elif way == 'N':
        x,y = x+dx[3]*int(dis),y+dy[3]*int(dis)
    else:
        x,y = x+dx[0]*int(dis),y+dy[0]*int(dis)

print(x,y)