temp = input().split()
n = int(temp[0])
k = int(temp[1])
T = list(temp[2])
arr = []

def start_with_T(word, T):
    for i in range(len(T)):
        if word[i] != T[i]:
            return 0
    return 1

for _ in range(n):
    word = input()
    if start_with_T(word,T) == 1:
        arr.append(word)
    
arr.sort()
print(arr[k-1])