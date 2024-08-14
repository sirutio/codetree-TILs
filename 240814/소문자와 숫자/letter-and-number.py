s = input()

for char in s:
    if char.isalpha():
        print(char.lower(),end='')
    elif char.isdigit():
        print(char,end='')