n = int(input())
arr = list(map(int,input().split()))

for i in range(n):
    if i == 0:
        print(arr[0], end=' ')
    elif i%2 == 0:
        new_arr = arr[:i+1]
        new_arr.sort()
        print(new_arr[i//2], end=' ')