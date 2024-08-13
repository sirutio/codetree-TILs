string = list(input())
string[1] = 'a'
string[-2] = 'a'
tot = ''.join(string)
print(tot)