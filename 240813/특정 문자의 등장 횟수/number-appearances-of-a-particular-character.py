string = input()
cnt = 0
idx = string.find('ee')

while string[idx:].find('ee') != -1:
    curr = string[idx]+string[idx+1]
    if curr == 'ee':
        cnt += 1 
    idx += 1 
print(cnt,end=' ')

cnt = 0
idx = string.find('eb')

while string[idx:].find('eb') != -1:
    curr = string[idx]+string[idx+1]
    if curr == 'eb':
        cnt += 1 
    idx += 1 
print(cnt,end=' ')