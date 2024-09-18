class info:
    def __init__(self,date,day,weather):
        self.date = date
        self.day = day
        self.weather = weather
 
n = int(input())
arr = [tuple(input().split()) for _ in range(n)]
data = [info(date,day,weather) for date,day,weather in arr]

def IsRecent(y,m,d,recent_date):
    ry,rm,rd = recent_date[:4],recent_date[5:7], recent_date[8:]
    if int(y) < int(ry):
        if int(m) < int(rm):
            if int(d) < int(rd):
                return True
    return False

recent_idx = 0
recent_date = '2101-13-32'
for i,information in enumerate(data):
    if information.weather == 'Rain':
        date_str = information.date
        y,m,d = date_str[:4],date_str[5:7], date_str[8:]
        if IsRecent(y,m,d,recent_date):
            recent_idx = i
            recent_date = date_str 
    
print(data[recent_idx].date, data[recent_idx].day, data[recent_idx].weather)