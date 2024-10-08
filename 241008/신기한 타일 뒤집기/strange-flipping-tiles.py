'''
L 흰 R 검 현재 위치 포함
'''
OFFSET = 10
n = int(input())
cur = OFFSET
arr = [-1 for _ in range(OFFSET*2)]

for _ in range(n):
    x,way = input().split()
    if way == 'L':
        for i in range(int(x)):
            arr[cur-i] = 0
        cur -= int(x)-1
    else:
        for i in range(int(x)):
            arr[cur+i] = 1
        cur += int(x)-1

w,b = 0,0
for tile in arr:
    if tile == 1:
        b += 1
    elif tile == 0:
        w += 1
print(w,b)