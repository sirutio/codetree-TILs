s,q = input().split()
q = int(q)

for _ in range(q):
    question = int(input())
    if question == 1:
        s = s[1:]+s[0]
        print(s)
    elif question == 2:
        s = s[-1]+s[:-1] 
        print(s)
    else:  
        s = s[::-1]
        print(s)