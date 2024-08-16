def IsYoonNyeon(y):
    if y%100 == 0  and y%400 != 0:
        return False
    else:
        if y%4 == 0:
            return True
        else:
            return False


y = int(input())
if IsYoonNyeon(y):
    print('true')
else:
    print('false')