#import numpy as np
import pandas as pd
from textblob import TextBlob
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