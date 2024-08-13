A = input()
B = input()
cnt = 0

for i in range(len(A)-len(B)+1):
    IsIt = True
    for j in range(len(B)):
        if A[i+j] != B[j]:
            IsIt = False
            break
    if IsIt == True:
        cnt += 1
    
print(cnt)