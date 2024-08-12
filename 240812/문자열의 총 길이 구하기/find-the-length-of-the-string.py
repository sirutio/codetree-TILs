string = input().split()
sum_val = 0

for word in string:
    sum_val += len(word)
print(sum_val)