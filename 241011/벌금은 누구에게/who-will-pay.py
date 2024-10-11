N,M,K = map(int,input().split())
punishment = [0]*N

punish = False
for _ in range(M):
    num = int(input())
    punishment[num-1] += 1
    if punishment[num-1] >= K:
        print(num)
        punish = True
        break

if not punish:
    print(-1)