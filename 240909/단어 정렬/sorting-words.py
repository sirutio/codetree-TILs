n = int(input())
arr = []
for i in range(n):
    word = input()
    arr.append(word)
arr.sort()

for word in arr:
    print(word)