def seq(N):
    if N == 0:
        return
    seq(N-1)
    print(N,end=' ')

def qes(N):
    if N == 0:
        return
    print(N,end=' ')
    qes(N-1)

N = int(input())
seq(N)
print()
qes(N)