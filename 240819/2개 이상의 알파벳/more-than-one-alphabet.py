def IsDifferent(string):
    arr = [0 for _ in range(26)]
    cnt = 0
    for char in string:
        idx = ord(char)-97
        if arr[idx] == 0:
            arr[idx] = 1
            cnt += 1
    if cnt >= 2:
        print('Yes')
    else:
        print('No')

A = input()
IsDifferent(A)