'''Checks price movement of a stock market ticker daily at 7AM; if change over 5%, sends an 
email including price movement and 3 most popular news headlines regarding the company, 
with links to articles.'''
import requests
from datetime import datetime, timedelta
import smtplib
import time

# stock/company variables - adjust accordingly
STOCK = "IBM"
COMPANY_NAME = "IBM"

# date variables
YESTERDAY = str(datetime.today().date() - timedelta(days=1))
TWO_PREV = str(datetime.today().date() - timedelta(days=2))

# smtp variables - adjust accordingly
SENDER_EMAIL_ADDR ='youremail@gmail.com'
SENDER_PW ='yourkey'
SENDER_SERVER = 'smtp.gmail.com'
SENDER_PORT = 587
SENDER_NAME = "yourname"

def sig_change():
    '''Checks whether company's stock price has moved by 5% and if so, returns the movement as a percentage.'''
    # stock api variables
    params = {
    'function' : 'TIME_SERIES_DAILY',
    'symbol' : STOCK,
    'apikey' : 'demo'
    }

    stock_api = 'https://www.alphavantage.co/query' # note - this API has rate limits
    response = requests.get(url=stock_api, params=params)
    response.raise_for_status()
    data = response.json()

    price_yesterday = float(data['Time Series (Daily)'][YESTERDAY]['4. close'])
    price_two_prev = float(data['Time Series (Daily)'][TWO_PREV]['4. close'])
    percent_change = round((price_yesterday - price_two_prev)/price_two_prev*100, 2)
    
    print(f"{STOCK} price movement: {percent_change}\n")

    if percent_change >= 5.0 or percent_change <= -5.0:
        return str(percent_change)
    
def get_news():
    '''Gets top 3 news articles for company and returns as 3 dicts'''
    # news_api variables
    news_key = '7569f3a469d44e5f9643268832a0f3ab'
    news_api = 'https://newsapi.org/v2/everything'

    params = {
        'apiKey' : news_key,
        'q' : COMPANY_NAME,
        'searchIn' : 'title',
        'sortBy' : 'popularity',
        'from' : TWO_PREV,
        'to' : YESTERDAY
    }

    response = requests.get(url=news_api, params=params)
    response.raise_for_status()
    data = response.json()
    return data['articles'][:3]

def send_email(percent_change, articles):
    '''Sends an email reporting the stock price change and news.'''
    message = f"Subject:{STOCK} Price Change: {percent_change}%\n\nTop 3 news stories for {STOCK}:\n\n"

    for article in articles:
        title = article['title']
        description = article['description']
        url = article['url']
        message = message + f'Headline: {title}\nDetail: {description}\nMore information: {url}\n\n'

    print(f"Sending email:\n\n{message}")
    
    with smtplib.SMTP(SENDER_SERVER, port=SENDER_PORT) as connection:
        connection.starttls()
        connection.login(user=SENDER_EMAIL_ADDR, password=SENDER_PW)
        connection.sendmail(
            from_addr=SENDER_EMAIL_ADDR, 
            to_addrs=SENDER_EMAIL_ADDR, 
            msg=message.encode('utf-8')
        )
    
    print("Email(s) successfully sent.")

# run check at 7AM each day
if __name__ == "__main__":
    while True:
        if datetime.now().hour == 7:
            print(f"Running check for {STOCK} price movement:")
            price_change = sig_change()
            if price_change:
                send_email(price_change, get_news())
            else:
                print(f"No significant price change detected.\n")
        else:
            print(f"Hour: {datetime.now().hour}. Check not run.\n")
        time.sleep(3600)