string = input()

for i,char in enumerate(string[::-1]):
    if len(string)%2 == 0:
        if i%2 == 0:
            print(char,end='')
    else:
        if i%2 != 0:
            print(char,end='')