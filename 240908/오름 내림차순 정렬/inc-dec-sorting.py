n = int(input())
arr = list(map(int,input().split()))
arr.sort()
for num in arr:
    print(num, end=' ')
print()
for num in arr[::-1]:
    print(num, end=' ')