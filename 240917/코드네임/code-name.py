class Person:
    def __init__(self,name,score):
        self.name = name
        self.score = score
    
inf = [tuple(input().split()) for _ in range(5)]
scorelist = []

for i in range(5):
    scorelist.append(int(inf[i][1]))

min_val = min(scorelist)
for i in range(5):
    if int(inf[i][1]) == min_val:
        print(inf[i][0], min_val)