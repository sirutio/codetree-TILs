def IsTargetNum(num):
    if In369(num) or IsMultiple3(num):
        return True 
    else:
        return False 

def In369(num):
    char = str(num)
    if '3' in char or '6' in char or '9' in char:
        return True 
    else:
        return False 

def IsMultiple3(num):
    if num%3 == 0:
        return True 
    else:
        return False 

a,b = map(int,input().split())
cnt = 0
for num in range(a,b+1):
    if IsTargetNum(num):
        cnt += 1
print(cnt)