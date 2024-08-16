def IsEvenMultiple5(n):
    if n%2 == 0:
        sum_val = 0
        sum_val = n//10+n%10
        if sum_val%5 == 0:
            print('Yes')
            return 0
    print('No')

n = int(input())
IsEvenMultiple5(n)