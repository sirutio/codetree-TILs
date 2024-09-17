class NextLevel:
    def __init__(self, ID=0, level=0):
        self.ID = ID
        self.level = level

First = NextLevel('codetree','10')
input_ = tuple(input().split())
Second = NextLevel()
Second.ID, Second.level = input_

print('user {0} lv {1}' .format(First.ID, First.level))
print('user {0} lv {1}' .format(Second.ID, Second.level))