def absolute(arr):
    for num in arr:
        if num < 0:
            print(-num,end=' ')
        else:
            print(num,end=' ')
N = int(input())
arr = map(int,input().split())
absolute(arr)