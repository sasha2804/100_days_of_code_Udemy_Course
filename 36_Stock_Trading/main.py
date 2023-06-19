import requests
from datetime import datetime, timedelta

import datetime as dt

# https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=TSLA&interval=5min&apikey=JDGNAXTOR66ZS312
demo = 'JDGNAXTOR66ZS312'

## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
# Dates definition
current_date = dt.datetime.now().date()
if current_date.weekday() != 5 and current_date.weekday() != 6:
    diff = 1
    diff1 = 1
    if current_date.weekday() == 0:
        diff = 3    
    last_date =  current_date - dt.timedelta(days=diff)

    if last_date == 0:
        diff1 = 3   
    prev_date = last_date - dt.timedelta(days=diff1)
print('last date: ', last_date) 
print('prev date: ', prev_date)

#  Getting data from Stock resource
STOCK_NAME = "TSLA"
PERIOD = "TIME_SERIES_DAILY_ADJUSTED"
url = f'https://www.alphavantage.co/query?function={PERIOD}&symbol={STOCK_NAME}&interval=5min&apikey={demo}'
response = requests.get(url)
response.raise_for_status()
data = response.json()

# Information for current date request
close_day_bef = float(data["Time Series (Daily)"][str(last_date)]["4. close"])
print('close chosen date: ',close_day_bef)

#TODO 2. - Get the day before yesterday's closing stock price
# print(data["Time Series (Daily)"]["2023-03-23"]["4. close"])
close_2days_bef = float(data["Time Series (Daily)"][str(prev_date)]["4. close"])
print('close date before: ',close_2days_bef)




#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
stock_diff = round(abs(close_day_bef-close_2days_bef))
print('difference: ', stock_diff)

#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
perc_diff = close_2days_bef/close_day_bef
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

# STOCK_NAME = "TSLA"
# PERIOD = "TIME_SERIES_DAILY_ADJUSTED"
KEY1 = '44268d9d294249ed9ed3044dbfd7e7c0'
url = f'https://newsapi.org/v2/everything?q=tesla&from=2023-05-19&sortBy=publishedAt&apiKey={KEY1}'
'https://newsapi.org/v2/everything?q=tesla&from=2023-05-19&sortBy=publishedAt&apiKey=44268d9d294249ed9ed3044dbfd7e7c0'
response_news = requests.get(url)
response_news.raise_for_status()
data_news = response_news.json()

#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.
headlines = [data_news["articles"][x]['title'] for x in range(4)]
print(headlines)

#TODO 9. - Send each article as a separate message via Twilio. 

'afasdfasf'

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

