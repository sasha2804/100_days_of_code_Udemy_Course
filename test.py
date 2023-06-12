from datetime import datetime, timedelta

import datetime as dt

current_date = dt.datetime.now()
cur_date = current_date.date()
current_week_day = current_date.weekday()

if current_week_day != 5 and current_week_day != 6:
    diff = 1
    if current_week_day == 0:
        diff = 3



previous_date = current_date - timedelta(days=diff)

print(type(current_date))

print(type(timedelta(days=diff)))




print(previous_date)






