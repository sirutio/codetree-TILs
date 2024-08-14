cnt = 0
arr = []
IsODD = True

while 1:
    put = input()
    if put == '0':
        break
    cnt += 1
    if IsODD == True:
        arr.append(put)
        IsODD = False
    else:
        IsODD = True
print(cnt)
for string in arr:
    print(string)