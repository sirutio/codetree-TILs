A = input()
B = input()
newA = ''
newB = ''

for char in A:
    if char.isdigit():
        newA += char
newA = int(newA)
for char in B:
    if char.isdigit():
        newB += char
newB = int(newB)

print(newA+newB)