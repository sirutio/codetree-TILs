a,b = input().split()
newa = ''
newb  = ''

for char in a:
    if not char.isdigit():
        break 
    newa += char
for char in b:
    if not char.isdigit():
        break 
    newb += char

print(int(newa)+int(newb))