import requests
import os
import datetime as dt
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla"
STOCK_API_KEY = os.environ["STOCK_API_KEY"]
FUNCTION = "TIME_SERIES_DAILY_ADJUSTED"

NEWS_API_KEY = os.environ['NEWS_API_KEY']

SMS_ACCOUNT_SID = os.environ['TWILIO_ACCOUNT_SID']
SMS_AUTH_TOKEN = os.environ['TWILIO_AUTH_TOKEN']

def format_message(yesterday_stock_end, two_days_ago_stock):
    diff = abs(yesterday_stock_end - two_days_ago_stock_end)
    if diff > 0:
        return "🔺"
    elif diff < 0:
        return "🔻"
    else:
        return "-"
    
## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 
def send_sms(sms_content):
    client = Client(SMS_ACCOUNT_SID, SMS_AUTH_TOKEN)
    message = client.messages \
        .create(
            body=sms_content,
            from_='+14846421849',
            to='+48792038802'
            )
    print(message.status)


## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
def get_news(diff_percentage, sign_inc_dec):
    url = f'https://newsapi.org/v2/top-headlines?q={COMPANY_NAME}&apiKey={NEWS_API_KEY}&country=us&category=business'
    r = requests.get(url)
    data = r.json()["articles"]
    sms_content = f"TSLA: {sign_inc_dec}{diff_percentage}\n"
    if len(data) > 0:
        for i in range (0,len(data)):
            sms_content += f'{i+1}. News:\nHeadline: {data[i]["title"]}\nBrief: {data[i]["description"]}\n\n'
    else:
        sms_content = "News API did not provide any article"
    print(sms_content)
    return sms_content


## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
yesterday_date = dt.date.today() - dt.timedelta(1)
two_days_ago_date = dt.date.today() - dt.timedelta(2)

url = f'https://www.alphavantage.co/query?function={FUNCTION}&symbol={STOCK}&apikey={STOCK_API_KEY}'
r = requests.get(url)
data = r.json()["Time Series (Daily)"]
if yesterday_date in list(data.keys()) and two_days_ago_date in list(data.keys()):
    yesterday_stock=list(data.keys())[yesterday_date]
    two_days_ago_stock=list(data.keys())[two_days_ago_date]
    print(f'{yesterday_stock}: {data[yesterday_stock]}')
    print(f'{two_days_ago_stock}: {data[two_days_ago_stock]}')
    yesterday_stock_end = float(data[yesterday_stock]["4. close"])
    two_days_ago_stock_end = float(data[two_days_ago_stock]["4. close"])
    diff = abs(yesterday_stock_end - two_days_ago_stock_end)
    diff_percentage = (diff / yesterday_stock_end) * 100
    print(diff_percentage)
    if diff_percentage > 1:
        sign_inc_dec = format_message(yesterday_stock_end, two_days_ago_stock_end)
        sms_content = get_news(diff_percentage, sign_inc_dec)
        send_sms(sms_content)
    else:
        print("STOCK price did not increase/decreases by at least 1% between yesterday and the day before yesterday")
else:
    latest_stock=list(data.keys())[0]
    befote_latest_stock=list(data.keys())[1]
    print("ERROR: There is no data for yesterday's or/and two days ago stock stock.\nLatest stock:")
    print(f'{latest_stock}: {data[latest_stock]}')
    print(f'{befote_latest_stock}: {data[befote_latest_stock]}')


#Optional: Format the SMS message like this: 

"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

