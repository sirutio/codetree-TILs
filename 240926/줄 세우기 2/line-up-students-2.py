N = int(input())
class student:
    def __init__(self,h,w,num):
        self.h = h
        self.w = w
        self.num = num

arr = []
for i in range(N):
    h,w = map(int,input().split())
    arr.append(student(h,w,i+1))

arr.sort(key=lambda x:(x.h,-x.w))

for person in arr:
    print(person.h,person.w,person.num)