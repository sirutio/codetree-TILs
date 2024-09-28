N = input()
num = 0

for digit in N:
    num = num*2 + int(digit)
num *= 17

dem = []
while 1:
    if num < 2:
        dem.append(num)
        break
    dem.append(num%2) 
    num //= 2
for digit in dem[::-1]:
    print(digit,end='')