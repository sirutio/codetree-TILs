N,B = map(int,input().split())
digit = []

while N > B:
    digit.append(N%B)
    N //= B
digit.append(N)
for num in digit[::-1]:
    print(num,end='')