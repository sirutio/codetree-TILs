n = int(input())
digit = []

while 1:
    if n < 2:
        digit.append(n)
        break
    digit.append(n%2)
    n = n // 2

for num in digit[::-1]:
    print(num, end='')