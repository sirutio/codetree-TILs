N,M = map(int,input().split())
A = [0]
B = [0]
ans = 0

# 배열 기록 
for _ in range(N):
    v,t = map(int,input().split())
    for _ in range(t):
        A.append(A[len(A)-1]+v)

for _ in range(M):
    v,t = map(int,input().split())
    for _ in range(t):
        B.append(B[len(B)-1]+v)

# 선두 체크 
first = 'N'
for i in range(1,len(A)):
    if A[i] > B[i] and first != 'A':
        ans += 1
        first = 'A'
    elif A[i] < B[i] and first != 'B':
        ans += 1
        first = 'B'
    elif A[i] == B[i] and first != 'AB':
        ans += 1
        first = 'AB'

print(ans)