class info:
    def __init__(self,date,day,weather):
        self.date = date
        self.day = day
        self.weather = weather
 
n = int(input())
arr = [tuple(input().split()) for _ in range(n)]
data = [info(date,day,weather) for date,day,weather in arr]

for i,information in enumerate(data):
    if information.weather == 'Rain':
        print(information.date, information.day, 'Rain')
        break