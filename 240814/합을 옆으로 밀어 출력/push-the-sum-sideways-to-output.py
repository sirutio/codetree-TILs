n = int(input())
sum_val = 0

for _ in range(n):
    num = int(input()) 
    sum_val += num 
sum_val = str(sum_val)
print(sum_val[1:]+sum_val[0])