n = int(input())
sum_val = 0
cnt = 0

for _ in range(n):
    string = input()
    if string[0] == 'a':
        cnt += 1
    sum_val += len(string)

print(sum_val, cnt)