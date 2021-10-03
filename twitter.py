#import numpy as np
import re
import nltk 
import pandas as pd
from textblob import TextBlob
from nltk import word_tokenize,sent_tokenize
from typing import Counter, List
from nltk.corpus import stopwords
from nltk.util import filestring, pr
"""
def processTweet(self,tweet):
    
     tweet = re.sub(r'\&\w*;', '', tweet)
    
     tweet = re.sub('@[^\s]+','',tweet)
    
     tweet = re.sub(r'\$\w*', '', tweet)
     tweet = re.lower()    
    
     tweet =re.sub(r'\s\s+', ' ', tweet)

     tweet = re.lstrip(' ') 

     return ''.join(c for c in tweet if c <= '\uFFFF') 
    """

dataset=pd.read_csv('twitter.csv' , engine='python')

#if @dataset is only of text and with no additional data

"""
and if data set consists of more columns
tweet_id,sentiment,content
1956967341,empty,@tiffanylue i know  i was listenin to bad habit earlier and i started freakin at his part =[
1956967666,sadness,Layin n bed with a headache  ughhhh...waitin on your call...
1956967696,sadness,Funeral ceremony...gloomy friday...
1956967789,enthusiasm,wants to hang out with friends SOON!
1956968416,neutral,"@dannycastillo We want to trade with someone who has Houston tickets, but no one will."
1956968477,worry,Re-pinging @ghostridah14: why didn't you go to prom? BC my bf didn't like my friends
1956968487,sadness,"I should be sleep, but im not! thinking about an old friend who I want. but he's married now. damn, &amp; he wants me 2! scandalous!"
1956968636,worry,Hmmm. http://www.djhero.com/ is down
1956969035,sadness,@charviray Charlene my love. I miss you
1956969172,sadness,@kelcouch I'm sorry  at least it's Friday?
"""
#then parse it by dataset>content

csv_text=[]
for i in dataset:#dataset['content']
    csv_text.append(i)

csv_words=[]
countsm=1
for i in csv_text:
    i = re.sub('[^a-zA-Z]',' ', i)
    i=i.replace('  ','')
    i=i.split()
    for f in i:
        if not f in set(stopwords.words('english')):
            csv_words.append(f)

print(csv_words)

x=dataset.iloc[:,5]
#df=pd.DataFrame(columns=[6])
   

pos=0
neg=0
neu=0
y=0

for tweet in x:
    y=y+1
    #tweet=processTweet(tweet)
    analysis = TextBlob(tweet) 
        
    if analysis.sentiment.polarity > 0: 
 #      dataset[x, 7]=1
     pos=pos+1
  #   ptweets= [ tweet for tweet in x  if analysis.sentiment.polarity > 0]
   #    df=df.apend(1)
    elif analysis.sentiment.polarity == 0:
   #   neutweets= [ tweet for tweet in x if analysis.sentiment.polarity == 0]
      neu=neu+1
    else:
       # dataset[x, 7]=-1
    #   ntweets= [ tweet for tweet in x if analysis.sentiment.polarity <-1 ]
       neg=neg+1
      #  df=df.apend(-1)
            
        
            
print("percentage of positive tweets")
print(pos*100/y)

print("percentage of negative tweets")
print(neg*100/y)

print("percentage of neutral tweets")
print(neu*100/y)
