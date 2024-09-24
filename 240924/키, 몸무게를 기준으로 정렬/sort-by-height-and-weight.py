n = int(input())
class person:
    def __init__(self,name,height,weight):
        self.name = name
        self.height = height
        self.weight = weight

arr = []
for _ in range(n):
    name,h,w = input().split()
    arr.append(person(name,int(h),int(w)))

arr.sort(key=lambda x:(x.height, -x.weight))

for p in arr:
    print(p.name, p.height, p.weight)