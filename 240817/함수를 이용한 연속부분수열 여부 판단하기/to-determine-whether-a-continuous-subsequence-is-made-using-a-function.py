def BinA(A,B):
    for i in range(len(A)-len(B)+1): 
        IsIt = True
        for j in range(i,i+len(B)):
            if A[j] != B[j-i]:
                IsIt = False
        if IsIt:
            return True
    return False

n1, n2 = map(int,input().split())
A = input().split()
B = input().split()

if BinA(A,B):
    print('Yes')
else:
    print('No')