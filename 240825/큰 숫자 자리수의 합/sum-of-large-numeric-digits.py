a,b,c = map(int,input().split())
value = a*b*c

def sum_val(val):
    if val//10 == 0:
        return val

    return sum_val(val//10) + val%10

print(sum_val(value))