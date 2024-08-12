string = input()
num = int(input())
if num >= len(string):
    end = -1
else:
    end = len(string)-num-1

for i in string[-1:end:-1]:
    print(i, end='')