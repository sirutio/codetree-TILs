m1,d1,m2,d2 = map(int, input().split())
arr = [31,28,31,30,31,30,31,31,30,31,30,31]

temp1 = 0
for i in range(m1-1):
    temp1 += arr[i]
temp1 += d1


temp2 = 0
for i in range(m2-1):
    temp2 += arr[i]
temp2 += d2

print(temp2-temp1+1)