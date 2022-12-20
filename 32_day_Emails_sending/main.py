# from multiprocessing import connection
# import smtplib

# my_email = "o.korotushko@gmail.com"
# password = "ipzxnpatikiynqti"
# message = 'Hello, here is test message last message'


# # with smtplib.SMTP("smtp.gmail.com") as connection:
# #     connection.starttls()
# #     connection.login(user=my_email, password=password)
# #     connection.sendmail(from_addr=my_email, to_addrs="o.korotushko@yahoo.com", msg=f"Subject:Hello\n\n{message}")
# #     # connection.close()


# connection =  smtplib.SMTP("smtp.gmail.com")
# connection.starttls()
# connection.login(user=my_email, password=password)
# connection.sendmail(from_addr=my_email, to_addrs="o.korotushko@yahoo.com", msg=f"Subject:Hello\n\n{message}")
# connection.close()


import datetime as dt
import pandas as pd
import random as rd

# now =  dt.datetime.now()
# day = now.weekday()
# print(now.year, now.month, now.day, day)


with open('32_day_Emails_sending/quotes.txt') as quotes:
    list = quotes.readlines()


print(list[0])

print('random: ',rd.choice(list))











