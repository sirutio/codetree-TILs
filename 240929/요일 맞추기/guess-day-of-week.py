m1, d1, m2, d2 = map(int,input().split())
Reversed = False
if m1 > m2:
    m1,m2 = m2,m1
    d1,d2 = d2,d1
    Reversed = True
days = [31,28,31,30,31,30,31,31,30,31,30,31]
day7 = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
gap = 0

for i in range(m1-1,m2-1):
    gap += days[i]
gap += d2-d1

if Reversed:
    print(day7[-gap%7])
else:
    print(day7[gap%7])