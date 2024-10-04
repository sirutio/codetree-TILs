n = int(input())
ans = 0
cnt = 0
num = 0

for _ in range(n):
    num_new = int(input())
    if num_new > num:
        cnt += 1
    else:
        cnt = 1
    ans = max(cnt, ans)
    num = num_new

print(ans)