'''
L = 흰, R = 검 / 현재 위치 포함 
각각 두번 이상 칠해지면 회색. 
'''
n = int(input())
whiteNblack = [[0,0] for _ in range(100*1000*2)]
white0black1 = [-1]*100*1000*2
colors = [0,0,0]
current_location = 100*1000

for _ in range(n):
    x, way = input().split()
    if way == 'L':
        for i in range(int(x)):
            whiteNblack[current_location-i][0] += 1
            white0black1[current_location-i] = 0
        current_location -= (int(x)-1)
    else:
        for i in range(int(x)):
            whiteNblack[current_location+i][1] += 1
            white0black1[current_location+i] = 1
        current_location += (int(x)-1)

for i in range(2*100*1000):
    if whiteNblack[i][0] >=2 and whiteNblack[i][1] >=2:
        colors[2] += 1
    else:
        if white0black1[i] == 0:
            colors[0] += 1
        elif white0black1[i] == 1:
            colors[1] += 1
print(colors[0], colors[1], colors[2])