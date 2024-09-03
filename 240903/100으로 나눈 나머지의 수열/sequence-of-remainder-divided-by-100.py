N = int(input())

def seq(N):
    if N == 1:
        return 2
    elif N == 2:
        return 4
    else:
        return (seq(N-1)*seq(N-2))%100

print(seq(N))