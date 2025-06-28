from datetime import *
import requests, os

STOCK_LIST = ["IBM", "Google", "Microsoft", "Sony", "Nintendo"]
ALPHA_VANTAGE_API_KEY = os.environ.get("day_36_alpha_vantage_api")
NEWS_API_KEY = os.environ.get("day_36_news_api")
THREE_DAYS_AGO = str(datetime.now() - timedelta(3)).split(" ")[0]

#Retrieves stock information and news for IBM
IBM_ALPHA_VANTAGE_API = requests.get(f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM"
                                 f"&apikey={ALPHA_VANTAGE_API_KEY}")
IBM_NEWS = requests.get(f"https://newsapi.org/v2/everything?q=ibm&from={THREE_DAYS_AGO}&pageSize=3&language=en&"
                        f"apiKey={NEWS_API_KEY}")
IBM_ALPHA_VANTAGE_API.raise_for_status()
IBM_NEWS.raise_for_status()
IBM_ALPHA_VANTAGE_API_DATA = IBM_ALPHA_VANTAGE_API.json()
IBM_NEWS_DATA = IBM_NEWS.json()

#Retrieves stock information and news for Google
GOOGLE_ALPHA_VANTAGE_API = requests.get(f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=GOOGL"
                                 f"&apikey={ALPHA_VANTAGE_API_KEY}")
GOOGLE_NEWS = requests.get(f"https://newsapi.org/v2/everything?q=google&from={THREE_DAYS_AGO}&pageSize=3&language=en"
                           f"&apiKey={NEWS_API_KEY}")
GOOGLE_ALPHA_VANTAGE_API.raise_for_status()
GOOGLE_NEWS.raise_for_status()
GOOGLE_ALPHA_VANTAGE_API_DATA = GOOGLE_ALPHA_VANTAGE_API.json()
GOOGLE_NEWS_DATA = GOOGLE_NEWS.json()

#Retrieves stock information and news for Microsoft
MICROSOFT_ALPHA_VANTAGE_API = requests.get(f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=MSFT"
                                 f"&apikey={ALPHA_VANTAGE_API_KEY}")
MICROSOFT_NEWS = requests.get(f"https://newsapi.org/v2/everything?q=microsoft&from={THREE_DAYS_AGO}&pageSize=3"
                              f"&language=en&apiKey={NEWS_API_KEY}")
MICROSOFT_ALPHA_VANTAGE_API.raise_for_status()
MICROSOFT_NEWS.raise_for_status()
MICROSOFT_ALPHA_VANTAGE_API_DATA = MICROSOFT_ALPHA_VANTAGE_API.json()
MICROSOFT_NEWS_DATA = MICROSOFT_NEWS.json()

#Retrieves stock information and news for Sony
SONY_ALPHA_VANTAGE_API = requests.get(f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=SONY"
                                 f"&apikey={ALPHA_VANTAGE_API_KEY}")
SONY_NEWS = requests.get(f"https://newsapi.org/v2/everything?q=sony&from={THREE_DAYS_AGO}&pageSize=3&language=en"
                         f"&apiKey={NEWS_API_KEY}")
SONY_ALPHA_VANTAGE_API.raise_for_status()
SONY_NEWS.raise_for_status()
SONY_ALPHA_VANTAGE_API_DATA = SONY_ALPHA_VANTAGE_API.json()
SONY_NEWS_DATA = SONY_NEWS.json()

#Retrieves stock information and news for Nintendo
NINTENDO_ALPHA_VANTAGE_API = requests.get(f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=NTDOY"
                                 f"&apikey={ALPHA_VANTAGE_API_KEY}")
NINTENDO_NEWS = requests.get(f"https://newsapi.org/v2/everything?q=nintendo&from={THREE_DAYS_AGO}&pageSize=3"
                             f"&language=en&apiKey={NEWS_API_KEY}")
NINTENDO_ALPHA_VANTAGE_API.raise_for_status()
NINTENDO_NEWS.raise_for_status()
NINTENDO_ALPHA_VANTAGE_API_DATA = NINTENDO_ALPHA_VANTAGE_API.json()
NINTENDO_NEWS_DATA = NINTENDO_NEWS.json()

bodyMessage = ""
def stockChecker(arg):
    global bodyMessage
    stockName = arg

    if stockName == "IBM":
        ticker = "IBM"
        dateList = list(IBM_ALPHA_VANTAGE_API_DATA["Time Series (Daily)"].keys())
        todayClose = IBM_ALPHA_VANTAGE_API_DATA["Time Series (Daily)"][dateList[0]]["4. close"]
        yesterdayClose = IBM_ALPHA_VANTAGE_API_DATA["Time Series (Daily)"][dateList[1]]["4. close"]
    elif stockName == "Google":
        ticker = "GOOGL"
        dateList = list(GOOGLE_ALPHA_VANTAGE_API_DATA["Time Series (Daily)"].keys())
        todayClose = GOOGLE_ALPHA_VANTAGE_API_DATA["Time Series (Daily)"][dateList[0]]["4. close"]
        yesterdayClose = GOOGLE_ALPHA_VANTAGE_API_DATA["Time Series (Daily)"][dateList[1]]["4. close"]
    elif stockName == "Microsoft":
        ticker = "MSFT"
        dateList = list(MICROSOFT_ALPHA_VANTAGE_API_DATA["Time Series (Daily)"].keys())
        todayClose = MICROSOFT_ALPHA_VANTAGE_API_DATA["Time Series (Daily)"][dateList[0]]["4. close"]
        yesterdayClose = MICROSOFT_ALPHA_VANTAGE_API_DATA["Time Series (Daily)"][dateList[1]]["4. close"]
    elif stockName == "Sony":
        ticker = "SONY"
        dateList = list(SONY_ALPHA_VANTAGE_API_DATA["Time Series (Daily)"].keys())
        todayClose = SONY_ALPHA_VANTAGE_API_DATA["Time Series (Daily)"][dateList[0]]["4. close"]
        yesterdayClose = SONY_ALPHA_VANTAGE_API_DATA["Time Series (Daily)"][dateList[1]]["4. close"]
    elif stockName == "Nintendo":
        ticker = "NTDOY"
        dateList = list(NINTENDO_ALPHA_VANTAGE_API_DATA["Time Series (Daily)"].keys())
        todayClose = NINTENDO_ALPHA_VANTAGE_API_DATA["Time Series (Daily)"][dateList[0]]["4. close"]
        yesterdayClose = NINTENDO_ALPHA_VANTAGE_API_DATA["Time Series (Daily)"][dateList[1]]["4. close"]

    if float(todayClose) > float(yesterdayClose):
        difference = float(todayClose) - float(yesterdayClose)
        percentChange = (difference / float(todayClose)) * 100
        bodyMessage += f"{ticker} 🔺{percentChange:.2f}%\n"
        bodyMessage += f"Today's {stockName} closing stock value: ${float(todayClose):.2f}\n"
        bodyMessage += f"Yesterday's {stockName} closing stock value: ${float(yesterdayClose):.2f}\n"
        bodyMessage += f"Stock value increased by ${difference:.2f}\n\n"
    if float(todayClose) < float(yesterdayClose):
        difference = float(yesterdayClose) - float(todayClose)
        percentChange = (difference / float(todayClose)) * 100
        bodyMessage += f"{ticker} 🔻{percentChange:.2f}%\n"
        bodyMessage += f"Today's {stockName} closing stock value: ${float(todayClose):.2f}\n"
        bodyMessage += f"Yesterday's {stockName} closing stock value: ${float(yesterdayClose):.2f}\n"
        bodyMessage += f"Stock value decreased by ${difference:.2f}\n\n"
    else:
        pass

newsMessage = ""
def news(arg):
    global newsMessage
    stockName = arg

    if stockName == "IBM":
        newsMessage += "*** IBM NEWS ***\n\n"
        for i in range(len(IBM_NEWS_DATA)):
            newsMessage += f"Headline: {IBM_NEWS_DATA['articles'][i]['title']}\nLink: {IBM_NEWS_DATA['articles'][i]['url']}\n\n"
    elif stockName == "Google":
        newsMessage += "*** GOOGLE NEWS ***\n\n"
        for i in range(len(GOOGLE_NEWS_DATA)):
            newsMessage += f"Headline: {GOOGLE_NEWS_DATA['articles'][i]['title']}\nLink: {GOOGLE_NEWS_DATA['articles'][i]['url']}\n\n"
    elif stockName == "Microsoft":
        newsMessage += "*** MICROSOFT NEWS ***\n\n"
        for i in range(len(MICROSOFT_NEWS_DATA)):
            newsMessage += f"Headline: {MICROSOFT_NEWS_DATA['articles'][i]['title']}\nLink: {MICROSOFT_NEWS_DATA['articles'][i]['url']}\n\n"
    elif stockName == "Sony":
        newsMessage += "*** SONY NEWS ***\n\n"
        for i in range(len(SONY_NEWS_DATA)):
            newsMessage += f"Headline: {SONY_NEWS_DATA['articles'][i]['title']}\nLink: {SONY_NEWS_DATA['articles'][i]['url']}\n\n"
    elif stockName == "Nintendo":
        newsMessage += "*** NINTENDO NEWS ***\n\n"
        for i in range(len(NINTENDO_NEWS_DATA)):
            newsMessage += f"Headline: {NINTENDO_NEWS_DATA['articles'][i]['title']}\nLink: {NINTENDO_NEWS_DATA['articles'][i]['url']}\n\n"

for i in STOCK_LIST:
    stockChecker(i)
    news(i)

bodyMessage += newsMessage

print(bodyMessage)