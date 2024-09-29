m1, d1, m2, d2 = map(int,input().split())
days = [31,28,31,30,31,30,31,31,30,31,30,31]
gap = 0
for i in range(m1-1,m2-1):
    gap += days[i]
gap += d2-d1 
day7 = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
print(day7[gap%7])