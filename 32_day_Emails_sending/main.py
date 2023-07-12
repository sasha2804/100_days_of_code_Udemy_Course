# from calendar import calendar
import datetime as dt
import random as rd
import smtplib

my_email = "o.korotushko@gmail.com"
password = "ipzxnpatikiynqti"
message = 'Hello, here is test message last message'


# reading list of phrases to send
with open('32_day_Emails_sending/quotes.txt') as quotes:
    phrases_set = quotes.readlines()

now =  dt.datetime.now()
day = now.weekday()

print(type(day))

trig = 1


# if day == 4:
if trig:
    message = rd.choice(phrases_set)
    print('message: ',message)
    connection =  smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs="o.korotushko@yahoo.com", msg=f"Subject:Motivation\n\n{message}")
    connection.close()


str1 = '2[]132123kom'
str2 = ''

for i in str1:
    if i.isalpha():
        str2 += i


print(str2)




