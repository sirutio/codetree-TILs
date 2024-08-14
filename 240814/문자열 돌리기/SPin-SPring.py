s = input()
L = len(s)
print(s)
for _ in range(L):
    s = s[-1] + s[:-1]
    print(s)