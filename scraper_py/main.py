import requests
import logging
import sys
import grpc
import pandas as pd
import numpy as np
import json
from types import SimpleNamespace
from concurrent import futures
from bs4 import BeautifulSoup
from datetime import datetime

from proto import news_pb2
from proto import news_pb2_grpc

from proto.news_pb2 import Analytics

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
    
    #split out words
    df['headlines'] = df['headlines'].str.lower().str.split()

    #wrangle words to be ready for json output
    all_words = df['headlines'].explode().to_list()
    final_df =pd.DataFrame(all_words, columns=['word'])
    final_df['scrape_datetime'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S") #"%d%m%Y"

    final_df['source'] = BBC
    final_df = final_df.to_json(orient="records")

    # print(final_df)
    final_df = json.loads(final_df)
    # x = Analytics(final_df[0])
    # return news_pb2.ScraperResponse(data=final_df)
    return final_df

# class Analytics(object):
#     def __init__(self, obj):
#         self.word = obj['word']
#         self.scrape_datetime = obj['scrape_datetime']
#         self.source = obj['source']

class Scrape(news_pb2_grpc.ProxyServicer):
    def getScraperData(self, request, context):
        return news_pb2.ScraperResponse(data=bbc_news_scraper())

def serve():
  server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
  news_pb2_grpc.add_ProxyServicer_to_server(
      Scrape(), server)
  server.add_insecure_port('[::]:50051')
  server.start()
  server.wait_for_termination()

if __name__ == '__main__':
    logging.basicConfig()
    serve()