A = input()
sum_val = 0

for char in A:
    if char.isdigit():
        sum_val += int(char)

print(sum_val)