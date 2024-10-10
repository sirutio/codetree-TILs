N = int(input())
ans, count = 1,0
arr = []

for i in range(N):
    temp = int(input())
    arr.append(temp)
    if i != 0 and temp != arr[i-1]:
        count = 0
    else:
        count += 1
    if ans < count:
            ans = count
    

print(ans)