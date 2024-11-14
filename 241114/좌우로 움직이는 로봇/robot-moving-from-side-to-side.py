n,m = map(int,input().split())
arrA = [0]
arrB = [0]

sec = 0
for i in range(n):
    t,d = input().split()
    t = int(t)
    if d == 'L':
        for i in range(1,t+1):
            arrA.append(arrA[sec+i-1]-1)
    else:
        for i in range(1,t+1):
            arrA.append(arrA[sec+i-1]+1)
    sec += t

sec = 0
for i in range(m):
    t,d = input().split()
    t = int(t)
    if d == 'L':
        for i in range(1,t+1):
            arrB.append(arrB[sec+i-1]-1)
    else:
        for i in range(1,t+1):
            arrB.append(arrB[sec+i-1]+1)
    sec += t

ans = 0
if len(arrA) > len(arrB):
    end = len(arrB)
    plus = arrA[end:]
    ended_loc = arrB[-1]
else:
    end = len(arrA)
    plus = arrB[end:]
    ended_loc = arrA[-1]

for i in range(2,end):
    if arrA[i-1] != arrB[i-1] and arrA[i] == arrB[i]:
        ans += 1
    
for i,loc in enumerate(plus):
    if loc == ended_loc and plus[i-1] != ended_loc:
        ans += 1

print(ans)
