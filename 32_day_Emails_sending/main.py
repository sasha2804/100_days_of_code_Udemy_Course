from multiprocessing import connection
import smtplib

my_email = "o.korotushko@gmail.com"
password = "ipzxnpatikiynqti"
message = 'Hello, here is test message last message'


# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email, to_addrs="o.korotushko@yahoo.com", msg=f"Subject:Hello\n\n{message}")
#     # connection.close()


connection =  smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email, password=password)
connection.sendmail(from_addr=my_email, to_addrs="o.korotushko@yahoo.com", msg=f"Subject:Hello\n\n{message}")
connection.close()




