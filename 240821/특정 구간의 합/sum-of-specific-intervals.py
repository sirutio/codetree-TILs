n,m = tuple(map(int,input().split()))
A = list(map(int,input().split()))

def sum_print(a1,a2):
    sum_val = 0
    for i in range(a1-1,a2):
        sum_val += A[i]
    print(sum_val)

for _ in range(m):
    a1,a2 = tuple(map(int,input().split()))
    sum_print(a1,a2)