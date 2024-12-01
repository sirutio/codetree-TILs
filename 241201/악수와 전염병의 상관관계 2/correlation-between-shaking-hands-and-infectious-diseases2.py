N,K,P,T = map(int,input().split())
infected = [0 for _ in range(N)]
can_infect = [K for _ in range(N)]
infected[P-1] = 1 

# 악수 정황 
shakes = []
for _ in range(T):
    handshake = tuple(map(int,input().split()))
    shakes.append(handshake)
shakes.sort()

for shake in shakes:
    person1,person2 = shake[1]-1, shake[2]-1
    if infected[person1] == infected[person2]: # 0,0 or 1,1
        if infected[person1] == 1:
            can_infect[person1] -= 1
            can_infect[person2] -= 1
    elif infected[person1] == 1 and can_infect[person1] > 0:
        can_infect[person1] -= 1
        infected[person2] = 1
    elif infected[person2] and can_infect[person2] > 0: 
        can_infect[person2] -= 1
        infected[person1] = 1

for person in infected:
    print(person,end='')


            
        

