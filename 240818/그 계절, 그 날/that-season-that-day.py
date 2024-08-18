def ThatSeason(y,m,d):
    if m > 12 or d > 31:
        return -1
    if m == 2:
        if (y%4 == 0 and y%400 == 0) or (y%4 == 0 and y%100 != 0):
            if d > 29:
                return -1
            else:
                return 'Winter'
        else: 
            if d > 28:
                return -1
            else:
                return 'Winter'
    if (m%2 == 0 and m < 8) or (m%2 != 0 and m > 8) and d > 30:
        return -1
    elif d > 31:
        return -1
    else:
        if m >= 3 and m <= 5:
            return 'Spring'
        elif m >= 6 and m <= 8:
            return 'Summer'
        elif m >= 9 and m <= 11:
            return 'Fall'
        else:
            return 'Winter'
     

Y,M,D = map(int,input().split())
print(ThatSeason(Y,M,D))