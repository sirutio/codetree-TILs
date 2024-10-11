N,M = map(int,input().split())
arrA = [0]
arrB = [0]

loc = 0
for _ in range(N):
    
    d,t = input().split()
    t = int(t)
    if d == 'L':
        for _ in range(t): #1~9
            loc -= 1
            arrA.append(loc)
    else:
        for _ in range(t): #1~9
            loc += 1
            arrA.append(loc)

loc = 0
for _ in range(M):
    d,t = input().split()
    t = int(t)
    if d == 'L':
        for _ in range(t): #1~9
            loc -= 1
            arrB.append(loc)
    else:
        for _ in range(t): #1~9
            loc += 1
            arrB.append(loc)

Meet = False
for i in range(1,len(arrA)):
    if arrA[i] == arrB[i]:
        print(i)
        Meet = True
        break

if not Meet:
    print(-1)