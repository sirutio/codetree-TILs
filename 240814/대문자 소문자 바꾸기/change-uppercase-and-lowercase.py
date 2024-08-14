s = input()

for char in s:
    if char >= 'A' and char <= 'Z':
        print(char.lower(),end='')
    else:
        print(char.upper(),end='')