string = input()
dx,dy = [1,0,-1,0], [0,-1,0,1]
x,y = 0,0
current_dir = 3 # 북쪽 
ans = 0

IsBack = False
for order in string:
    if order == 'L':
        current_dir = current_dir%4 - 1
    elif order == 'R': 
        current_dir = (current_dir+1)%4 
    else:
        x,y = x+dx[current_dir], y+dy[current_dir]
        if x == 0 and y == 0:
            print(ans+1)
            IsBack = True
            break
    ans += 1
if not IsBack:
    print(-1)
