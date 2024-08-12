string = [input() for _ in range(10)]
char = input()
IsThere = False

for word in string:
    if word[-1] == char:
        print(word)
        IsThere = True
    
if IsThere == False:
    print('None')