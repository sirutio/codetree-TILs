def decimal(num):
    IsDecimal = True
    if num == 1:
        IsDecimal = False
    for i in range(2,num//2+1):
        if num%i == 0:
            IsDecimal = False 
    return IsDecimal

def digitsum_even(num):
    sum_val = 0
    while num != 0:
        sum_val += num%10
        num //= 10
    if sum_val%2 == 0:
        return True
    else:
        return False

a,b = map(int,input().split())
cnt = 0

for num in range(a,b+1):
    if decimal(num):
        if digitsum_even(num):
            cnt += 1

print(cnt)