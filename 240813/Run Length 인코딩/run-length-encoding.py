A = input()
cnt = 2
new = []

for i in range(len(A)):
    if i != 0 and i != len(A)-1 and A[i] == A[i+1]:
        cnt += 1
    else:
        if i != 0:
            new.append(A[i])
            new.append(cnt)
            cnt = 1 
        else:
            continue

print(len(new))
for i in new:
    print(i,end='')