a,b,c = input(), input(), input()
lens = list([len(a), len(b), len(c)])
print(max(lens)-min(lens))