def sum_(N):
    sum_val = 0
    for i in range(1,N+1):
        sum_val += i
    return sum_val

N = int(input())
total = sum_(N)
print(total//10)