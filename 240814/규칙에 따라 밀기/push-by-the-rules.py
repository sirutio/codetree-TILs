A = input()
order = input()

for char in order:
    if char == 'L':
        A = A[1:]+A[0]
    else:
        A = A[-1]+A[0:-1]

print(A)