n,m = map(int,input().split())
A = list(map(int,input().split()))
sum_val = A[0]

while m != 1:
    sum_val += A[m-1]
    if m%2 == 0:
        m = m//2
    else:
        m -= 1
    
print(sum_val)