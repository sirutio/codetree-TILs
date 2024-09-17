class bomb:
    def __init__(self,code=0,color=0,sec=0):
        self.code = code
        self.color = color
        self.sec = sec
    
bomb = bomb()
bomb.code, bomb.color, bomb.sec = input().split()
print(f'code : {bomb.code}')
print(f'color : {bomb.color}')
print(f'second : {bomb.sec}')