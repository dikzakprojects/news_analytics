import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
url='https://www.bbc.com/news'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')
# headlines = soup.find('body').find_all('h3', class_ = 'gs-c-promo-heading__title')
BBC = "BBC"

#BBC Scraper
def bbc_news_scraper():
    news_list = []

    # Finds all the headers in BBC Home
    for h in soup.find('body').find_all('h3', class_ = 'gs-c-promo-heading__title'):
        news_title = h.contents[0].lower()

        if news_title not in news_list:
            if 'bbc' not in news_title:
                news_list.append(news_title)

    df=pd.DataFrame(news_list, columns=['headlines'])
    df['scrape_time'] = datetime.now()
    df['source'] = BBC
    return df
print(bbc_news_scraper())
