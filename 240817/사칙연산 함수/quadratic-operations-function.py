def plus(a,b):
    print(a,'+',b,'=',a+b)
    
def minus(a,b):
    print(a,'-',b,'=',a-b)

def divide(a,b):
    print(a,'/',b,'=',a//b)

def multiple(a,b):
    print(a,'*',b,'=',a*b)

a,o,b = input().split()
a = int(a)
b = int(b)

if o == '+':
    plus(a,b)
elif o == '-':
    minus(a,b)
elif o == '/':
    divide(a,b)
elif o == '*':
    multiple(a,b)
else:
    print('False')