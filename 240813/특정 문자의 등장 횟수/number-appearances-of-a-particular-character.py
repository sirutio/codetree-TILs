string = input()
cnt = 0
idx = string.index('ee')

while string[idx:].find('ee') != -1:
    idx += 1 
    cnt += 1 
print(cnt,end=' ')

cnt = 0
idx = string.index('eb')

while string[idx:].find('eb') != -1:
    idx = string.index('eb') + 1 
    cnt += 1 
print(cnt,end=' ')