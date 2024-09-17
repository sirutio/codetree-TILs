class thing:
    def __init__(self, name=0, code=0):
        self.name = name
        self.code = code
    
thing1 = thing('codetree', '50')
thing2 = thing()
thing2.name, thing2.code = input().split()
print(f'product {thing1.code} is {thing1.name}')
print(f'product {thing2.code} is {thing2.name}')