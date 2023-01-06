import pandas as pd
import datetime as dt
import random
import smtplib

# Get current date
now =  dt.datetime.now()
check_date = str(now.month) + str(now.day)
# Reading data 
df = pd.read_csv('32_day_Emails_sending/Challenge/birthdays.csv')
# Preparing dataframe for comparison
df['date_test'] = df['month'].astype(str) + df['date'].astype(str)
#  Make comparison and send email
name = ''
name_temp = ''
if check_date in df['date_test'].values:  
    names_list = (df[df['date_test'] == check_date]['Name'].values)
    for name in names_list:
        # Import text from random letter
        letter_number = random.randint(1,3)
        rand_letter = f'letter_{letter_number}.txt'
        with open(f'32_day_Emails_sending/Challenge/letter_templates/{rand_letter}') as letter:
            message = letter.read()
            message = message.replace("[NAME]", name) 
        # Sending email
        my_email = "o.korotushko@gmail.com"        
        recipient = (df[df['Name'] == name]['Email'].values)       
        password = "rctqqxhnzndqlteq"
        connection =  smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=recipient, msg=f"Subject:Happy Birthday!!!\n\n{message}")
        connection.close()
