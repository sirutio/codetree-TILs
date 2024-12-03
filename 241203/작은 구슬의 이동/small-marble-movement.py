n,t = map(int,input().split())
r,c,d = input().split()
r,c = int(r), int(c)
dxs,dys = [0,1,0,-1],[1,0,-1,0]
CharToInt = {
    'U' : 0,
    'R' : 1,
    'D' : 2,
    'L' : 3
}
dir_num = CharToInt[d]

# 격자 범위 확인 
def in_range(x,y):
    return x > 0 and x < n and y > 0 and y < n 

# t초간 이동
while t > 0:
    r,c = r+dxs[dir_num], c+dys[dir_num]
    # 벽에 부딪힘 
    if not in_range(r,c):
        t -= 1
        dir_num = 3-dir_num
        r,c = r+dxs[dir_num], c+dys[dir_num]
    t -= 1

print(r,c)