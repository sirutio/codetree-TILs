class person:
    def __init__(self,name,height,weight):
        self.name = name
        self.height = height
        self.weight = weight

arr = []
for _ in range(5):
    name,h,w = input().split()
    arr.append(person(name,int(h),float(w)))

arr.sort(key=lambda x:x.name)
print('name')
for human in arr:
    print(human.name,human.height,human.weight)

arr.sort(key=lambda x:-x.height)
print()
print('height')
for human in arr:
    print(human.name,human.height,human.weight)