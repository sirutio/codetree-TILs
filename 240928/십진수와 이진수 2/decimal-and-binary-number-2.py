N = input()
num = 0
i = 0

for digit in N[::-1]:
    num += int(digit)*(2**i)
    i += 1
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