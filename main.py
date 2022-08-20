import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import numpy as np

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
    
    df['headlines'] = df['headlines'].str.lower().str.split()
    all_words = df['headlines'].explode().to_list()

    final_df =pd.DataFrame(all_words, columns=['words'])
    # headline_words = df['headlines'].tolist()
    # words = pd.value_counts(np.array(headline_words))
    # words_ez = np.array(all_words)
    
    final_df['scrape_time'] = datetime.now()
    final_df['source'] = BBC

    final_df =final_df.to_json(orient="split")
    

    print(final_df)




    # df_json = df.to_json(orient='index')
    # return df


print(bbc_news_scraper())
