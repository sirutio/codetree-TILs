string = input()

for i,char in enumerate(string[::-1]):
    if i%2 == 0:
        print(char,end='')