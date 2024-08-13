n = int(input())
tot = ''

put = input().split()
tot = ''.join(put)
    

cnt = 0
for i in tot:
    cnt += 1
    print(i, end='')
    if cnt == 5:
        cnt = 0
        print()