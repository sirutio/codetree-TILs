string = input()
cnt = 0
idx = 0

while string[idx:].find('ee') != -1:
    idx = string.index('ee') + 1 
    cnt += 1 
print(cnt,end=' ')
while string[idx:].find('eb') != -1:
    idx = string.index('eb') + 1 
    cnt += 1 
print(cnt,end=' ')