# from datetime import datetime, timedelta

# import datetime as dt

# current_date = dt.datetime.now()
# cur_date = current_date.date()
# current_week_day = current_date.weekday()

# if current_week_day != 5 and current_week_day != 6:
#     diff = 1
#     if current_week_day == 0:
#         diff = 3



# previous_date = current_date - timedelta(days=diff)

# print(type(current_date))

# print(type(timedelta(days=diff)))




# print(previous_date)


# newlist = [x for x in range(10)]

# print(newlist)



# from calendar import calendar
import datetime as dt
import random as rd
import smtplib

my_email = "o.korotushko@gmail.com"
password = "ipzxnpatikiynqti"
message = 'Hello, here is test message last message'


trig = 1

if trig:
    connection =  smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs="o.korotushko@yahoo.com", msg=f"Subject:Motivation\n\n{message}")
    connection.close()







