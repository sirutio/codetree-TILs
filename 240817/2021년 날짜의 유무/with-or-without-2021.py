def IsThere(M,D):
    if M > 12 or D > 31:
        return False
    elif M == 2 and D > 28:
        return False

    if (M%2 == 0 and M < 8) or (M%2 != 0 and M > 8) and D > 30:
        return False
    elif D > 31:
        return False
    else:
        return True
     

M, D = map(int,input().split())

if IsThere(M,D):
    print('Yes')
else:
    print('No')