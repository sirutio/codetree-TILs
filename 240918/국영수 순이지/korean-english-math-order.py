n = int(input())
arr = [tuple(input().split()) for _ in range(n)]

arr.sort(key=lambda x:(-int(x[1]),-int(x[2]),-int(x[3])))

for name, kor, eng, math in arr:
    print(name,kor,eng,math)