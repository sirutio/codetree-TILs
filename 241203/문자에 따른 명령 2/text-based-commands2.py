x,y = 0,0
dir_num = 0
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

orders = input()
for order in orders:
    if order == 'L':
        dir_num = (dir_num-1+4)%4
    elif order == 'R':
        dir_num = (dir_num+1)%4
    else:
        x,y = x+dx[dir_num],y+dy[dir_num]

print(x,y)
