s = list(input())

while len(s) != 1:
    idx = int(input())
    if idx >= len(s):
        s.pop(-1)
    else:
        s.pop(idx)
    print(''.join(s))