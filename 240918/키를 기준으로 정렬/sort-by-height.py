n = int(input())
arr = [tuple(input().split()) for _ in range(n)]

arr.sort(key=lambda x:int(x[1]))

for name,height,weight in arr:
    print(name, height, weight)