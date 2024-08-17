def IsPalindrome(A):
    revA = A[::-1]
    if revA == A:
        return True
    else:
        return False

A = input()

if IsPalindrome(A):
    print('Yes')
else:
    print('No')