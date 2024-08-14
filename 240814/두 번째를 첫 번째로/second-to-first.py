s = list(input())
target = s[1]
change = s[0]

for i in range(len(s)):
    if s[i] == target:
        s[i] = change
    
print(''.join(s))