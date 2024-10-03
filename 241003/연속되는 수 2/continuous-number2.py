N = int(input())
arr = []
for _ in range(N):
    num = int(input())
    arr.append(num)

count = 0
ans = 1
for i in range(N):
    if i == 0 or arr[i] == arr[i-1]:
        count += 1
    else:
        count = 1
    if count > ans:
            ans = count
        
print(ans)