N = int(input())
arr = []

for i in range(N):
    x,y = map(int,input().split())
    arr.append((x,y,i+1))

arr.sort(key=lambda x:((abs(x[0])+abs(x[1])),i))

for tuple_ in arr:
    print(tuple_[2])