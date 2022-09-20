from datetime import datetime
import calendar
month_list = []
for i in range(1,13):
    date = datetime(year=2022,month=i,day=1)
    month_list.append(calendar.month_name[date.month])
print(month_list)