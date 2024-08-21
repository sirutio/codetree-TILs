def power(N):
    if N < 10:
        return N**2
    return power(N//10) + (N%10)**2

N = int(input())
print(power(N))