import requests
from datetime import datetime, timedelta
import smtplib
import datetime as dt

# https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=TSLA&interval=5min&apikey=JDGNAXTOR66ZS312
demo = 'JDGNAXTOR66ZS312'

## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]

#  Getting data from Stock resource
STOCK_NAME = "TSLA"
PERIOD = "TIME_SERIES_DAILY_ADJUSTED"
url = f'https://www.alphavantage.co/query?function={PERIOD}&symbol={STOCK_NAME}&interval=5min&apikey={demo}'
response = requests.get(url)
response.raise_for_status()
data = response.json()

# Dates definition
def date_define(date_input):
    current_date = date_input
    diff = 1    
    if current_date.weekday() == 0:
        diff = 3 
    last_date =  current_date - dt.timedelta(days=diff)
    return last_date

current_date = dt.datetime.now().date() - dt.timedelta(days=0)

#TODO 2. - Get the day before yesterday's closing stock price 
if current_date.weekday() != 5 and current_date.weekday() != 6:
    try:
        minus_day = date_define(current_date)
        # print('minus one day date: ', minus_day)
        minus_day_data = float(data["Time Series (Daily)"][str(minus_day)]["4. close"])
        print(f'date {minus_day} stocks close price: ', minus_day_data)
    except KeyError:
        print('Minus one day data are not in the table')  
        minus_day = date_define(current_date - dt.timedelta(days=1))
        # print('!!!!!! minus one day date corrected: ', minus_day)
        minus_day_data = float(data["Time Series (Daily)"][str(minus_day)]["4. close"])
        print(f'date {minus_day} stocks close price: ', minus_day_data)
    try:        
        minus_2days = date_define(minus_day)
        # print('minus 2 days day date: ', minus_2days)
        minus_2days_data = float(data["Time Series (Daily)"][str(minus_2days)]["4. close"])
        print(f'date {minus_2days} stocks close price: ',minus_2days_data)
    except KeyError:
        print('Minus 2 days data are not in the table')
        # print('test: ', minus_day)
        minus_2days = date_define(minus_day- dt.timedelta(days=1))
        # print('!!!!!! minus 2 days date corrected: ', minus_2days)
        minus_2days_data = float(data["Time Series (Daily)"][str(minus_2days)]["4. close"])
        print(f'date {minus_2days} stocks close price: ',minus_2days_data)  
 

#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
stock_diff = round(abs(minus_day_data-minus_2days_data))
print('difference: ', stock_diff)

#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
perc_diff = minus_day_data/minus_2days_data
if perc_diff < 1:
    perc_print = round((1 - perc_diff)*100)
else: 
    perc_print = round((perc_diff - 1)*100)
print(f'difference percentage: {perc_print}%')

#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").

    ## STEP 2: https://newsapi.org/ 
    # API key 44268d9d294249ed9ed3044dbfd7e7c0
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

STOCK_NAME = "TSLA"
PERIOD = "TIME_SERIES_DAILY_ADJUSTED"
KEY1 = '44268d9d294249ed9ed3044dbfd7e7c0'
url = f'https://newsapi.org/v2/everything?q=tesla&from={current_date-dt.timedelta(days=7)}&sortBy=publishedAt&apiKey={KEY1}'
'https://newsapi.org/v2/everything?q=tesla&from=2023-05-19&sortBy=publishedAt&apiKey=44268d9d294249ed9ed3044dbfd7e7c0'
response_news = requests.get(url)
response_news.raise_for_status()
data_news = response_news.json()


#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.
headlines = [data_news["articles"][x]['title'] for x in range(5)]
# print('HEADLINES: ',headlines)

#TODO 9. - Send each article as a separate message via Twilio. 
description = [data_news["articles"][x]['description'] for x in range(5)]
# print('DESCRIPTION: ',description)
print(f'{headlines[0]} \n {description[0]}')

my_email = "o.korotushko@gmail.com"
password = "ipzxnpatikiynqti"
message = 'Hello, here is test message last message'



if len(headlines) != 0:   
    connection =  smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs="o.korotushko@yahoo.com", msg=f"Subject:Motivation\n\n{message}")
    connection.close()


#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

