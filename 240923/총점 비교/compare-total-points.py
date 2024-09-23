n = int(input())
class student:
    def __init__(self,name=0,score1=0,score2=0,score3=0):
        self.name = name
        self.score1 = score1
        self.score2 = score2
        self.score3 = score3

arr = []
for i in range(n):
    name, score1, score2, score3 = tuple(input().split())
    arr.append(student(name,int(score1),int(score2), int(score3)))
arr.sort(key=lambda x: x.score1+x.score2+x.score3)

for i in range(n):
    print(arr[i].name, arr[i].score1, arr[i].score2, arr[i].score3)