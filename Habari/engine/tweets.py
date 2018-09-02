import tweepy
from textblob import TextBlob

# Step 1 - Authenticate
consumer_key= 'IAIdgkt1MC3EyLajgv5pDHfBb'
consumer_secret= '10MEU590Y5QlsnNH5qpwM22qf3gFr5mEDGPYFfRkoK6WgBli3d'

access_token='1014057072789540864-P2BrmDNt4AaF2R2x1apR37fYyrccsC'
access_token_secret='1eAwiYFrlLIftrzoIuDKSvtBPRMg3KFPqdezCbrn7K2bI'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#Step 3 - Retrieve Tweets
public_tweets = api.search('')



#CHALLENGE - Instead of printing out each tweet, save each Tweet to a CSV file
#and label each one as either 'positive' or 'negative', depending on the sentiment 
#You can decide the sentiment polarity threshold yourself


for tweet in public_tweets:
    print(tweet.text)
    
    #Step 4 Perform Sentiment Analysis on Tweets
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    print("")
