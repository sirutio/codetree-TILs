A = input()
cnt = 0
new = []

for i in range(len(A)):
    if i != len(A)-1 and A[i] == A[i+1]:
        cnt += 1
    else:
        cnt += 1
        new.append(A[i])
        new.append(cnt)
        cnt = 0

print(len(new))
for i in new:
    print(i,end='')