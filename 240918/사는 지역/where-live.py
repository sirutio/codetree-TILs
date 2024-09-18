class person:
    def __init__(self,name=0,local=0,region=0):
        self.name = name
        self.local = local
        self.region = region

n = int(input())
arr = [tuple(input().split()) for _ in range(n)]
people = [person(name,local,region) for name, local, region in arr]

target_idx = 0
for i,Person1 in enumerate(people):
    if Person1.name > people[target_idx].name:
        target_idx = i 

print('name', people[target_idx].name)
print('addr', people[target_idx].local)
print('city', people[target_idx].region)