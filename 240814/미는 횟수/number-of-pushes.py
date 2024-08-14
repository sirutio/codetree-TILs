A = input()
B = input()
IsPossible = False
n = 0

for _ in range(len(A)):
    A = A[-1]+A[:-1]
    n += 1
    if A == B:
        IsPossible = True
        break

if IsPossible == True:
    print(n)
else:
    print(-1)