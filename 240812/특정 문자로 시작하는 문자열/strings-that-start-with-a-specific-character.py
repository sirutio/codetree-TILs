n = int(input())
string = [input() for _ in range(n)]
char = input()
cnt = 0
aver = 0

for word in string:
    if word[0] == char:
        cnt += 1
        aver += len(word)
    
print(cnt, f'{aver/cnt:.2f}')