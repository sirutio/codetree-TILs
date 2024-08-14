n, A = input().split()
n = int(n)
cnt = 0

for _ in range(n):
    put = input()
    if A == put:
        cnt += 1

print(cnt)