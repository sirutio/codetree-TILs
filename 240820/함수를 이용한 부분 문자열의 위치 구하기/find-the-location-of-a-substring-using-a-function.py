A = input()
target = input()

def Find():
    for i in range(0,len(A)-len(target)+1):
        Isit = True
        for j in range(len(target)):
            if A[i+j] != target[j]:
                Isit = False
                break
        if Isit == True:
            print(i)
            break
    if Isit == False:
        print(-1) 

Find()