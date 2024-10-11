N,M = map(int,input().split())
arrA = [0]
arrB = [0]

sec = 0
for _ in range(N):
    v,t = map(int,input().split())
    for i in range(sec+1,sec+t+1):
        arrA.append(arrA[i-1]+v)
    sec += t
    
sec = 0
for _ in range(M):
    v,t = map(int,input().split())
    for i in range(sec+1,sec+t+1):
        arrB.append(arrB[i-1]+v)
    sec += t

ans = -1
first = 'N'
for i in range(len(arrA)):
    if arrA[i] > arrB[i] and arrA[i-1] <= arrB[i-1] and first != 'A':
        ans += 1
        first = 'A' 
    elif arrA[i] < arrB[i] and arrA[i-1] >= arrB[i-1] and first != 'B':
        ans += 1
        first = 'B'
    
print(ans)