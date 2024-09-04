N = int(input())

def seq(N):
    if N == 1:
        return 1
    elif N == 2:
        return 2
    else:
        return seq(N//3) + seq(N-1)
    
print(seq(N))