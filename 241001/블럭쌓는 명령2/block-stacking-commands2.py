N, K = map(int,input().split())
arr = [0 for _ in range(N)]

for _ in range(K):
    A,B = map(int,input().split())
    for i in range(A-1,B):
        arr[i] += 1
    
print(max(arr))