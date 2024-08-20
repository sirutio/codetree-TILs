def HelloWorld(N):
    if N == 0:
        return
    print('HelloWorld')
    HelloWorld(N-1)

N = int(input())
HelloWorld(N)