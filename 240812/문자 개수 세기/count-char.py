string = input()
alphabet = input()
cnt = 0

for char in string:
    if char == alphabet:
        cnt += 1 
print(cnt)