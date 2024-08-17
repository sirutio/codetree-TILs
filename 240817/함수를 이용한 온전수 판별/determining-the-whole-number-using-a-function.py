def Onjeonsoo(num):
    if num%2 != 0 and num%10 != 5:
        if num%3 == 0 and num%9 != 0:
            return True
    else:
        return False

a,b = map(int,input().split())
cnt = 0

for num in range(a,b+1):
    if Onjeonsoo(num):
        cnt += 1
    
print(cnt)