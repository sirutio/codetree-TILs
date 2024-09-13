class zero07:
    def __init__(self,c,p,t):
        self.code = c
        self.place = p 
        self.time = t 

input_ = input().split()
Secret = zero07(input_[0], input_[1], input_[2])

print('secret code :', Secret.code)
print('meeting point :', Secret.place)
print('time :', Secret.time)