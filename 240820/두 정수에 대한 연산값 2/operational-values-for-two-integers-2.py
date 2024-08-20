def printf(a,b):
    if a > b:
        a *= 2
        b += 10
    else:
        a += 10
        b *= 2
    print(a,b)

a,b = map(int, input().split())
printf(a,b)