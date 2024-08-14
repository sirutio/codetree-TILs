s, q = input().split()
q = int(q)

for _ in range(q):
    s = list(s)
    question = input().split()
    if question[0] == '1':
        a = int(question[1])
        b = int(question[2])
        s[a-1], s[b-1] = s[b-1], s[a-1]
        s = ''.join(s)
        print(s)
    else:
        s = list(s)
        a = question[1]
        b = question[2]
        for i in range(len(s)):
            if s[i] == a:
                s[i] = b
        s = ''.join(s)
        print(s)