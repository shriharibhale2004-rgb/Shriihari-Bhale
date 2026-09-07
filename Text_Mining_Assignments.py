# -*- coding: utf-8 -*-
"""
Created on Fri May 22 16:11:00 2026

@author: HP
"""

from bs4 import BeautifulSoup as bs
import requests
link="https://en.wikipedia.org/wiki/BCCI"
page=requests.get(link)
page
page.content
soup=bs(page.content, 'html.parser')
print(soup.prettify())
title=soup.find_all('p',class_='MKifs6 ojKp6')
title
review_title=[]
for i in range(0,len(title)):
    review_title.append(title[i].get_text())
review_title
len(review_title)
#we got 10 review title
rating=soup.find_all('div',class_='MKifs6 ojKp6')
rating
rate=[]
for i in range(0,len(rating)):
    rate.append(rating[i].get_text())
rate
len(rate)
#Now let us scrap the review body
review=soup.find_all('div',calss_='G4PxIA')
review
review_body=[]
for i in range(0,len(review)):
    review_body.append(review[i].get_text())
review_body
len(review_body)
#we got 10 review_body
import pandas as pd
df=pd.DataFrame()
df['review_title']=review_title
df['Rate']=rate
df['review']=review_body
df
################
#to create .csv file
df.to_csv("BCCI_reviews.csv",index=True)
###########
#sentiment analysis
import pandas as pd
from textblob import TextBlob
sent="This is very excellent garden"
pol=TextBlob(sent).sentiment.polarity
pol
df=pd.read_csv("flipkart_reviews.csv")
df.head()
df['polarity']=df['Review'].apply(lambda x:TextBlob(str(x)).sentiment.polarity)
df['polarity']
####################
