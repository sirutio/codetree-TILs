a,b = map(int,input().split())
n = input()

decimal = 0
for digit in n:
    decimal = decimal*a + int(digit)

arr = [] 
while decimal > 0:
    arr.append(decimal%b)
    decimal //= b

for i in arr[::-1]:
    print(i,end='')