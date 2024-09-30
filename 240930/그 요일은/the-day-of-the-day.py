m1, d1, m2, d2 = map(int,input().split())
days = [31,29,31,30,31,30,31,31,30,31,30,31]
A = input()
gap = d2-d1
for i in range(m1-1,m2-1):
    gap += days[i]

day7 = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
ans = gap//7
if A in day7[:gap%7+1]:
    ans += 1
print(ans)