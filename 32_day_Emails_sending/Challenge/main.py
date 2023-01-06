##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv DONE
# 2. Check if today matches a birthday in the birthdays.csv
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# 4. Send the letter generated in step 3 to that person's email address.


#TODO 1 read csv -> make DataFrame DONE
#TODO 2 make search in date column DataFrame DONE
#TODO 3 import text from random letter
#TODO 4 replace PLACE HOLDER in the letter with data from DataFrame
#TODO 5 send Email


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
            text = letter.readlines()        

        # Preparing message for email
        message = ''
        for line in text:
            message += line
            
        # Insertion of recipients name into the letter    
        message = message.replace('[NAME]', name) 

        # Sending email
        my_email = "o.korotushko@gmail.com"        
        recipient = (df[df['Name'] == name]['Email'].values)       
        password = "ipzxnpatikiynqti"
        connection =  smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=recipient, msg=f"Subject:Happy Birthday!!!\n\n{message}")
        connection.close()
