import tweepy
from tweepy.streaming import StreamListener
from textblob import TextBlob
import csv

consumer_key='zZWPaXgIgmohaSfFOM8U8xMu1'
consumer_secret='6qMhIv4LUMKYw9JRn386AxudWQCN6NWGQ5WgOiiuDn2csTYq8D'

access_token='2264037373-So8YG6aVSLKgHaNGVGKoiaK3yJBxphunxgkY0Qd'
access_token_secret='eJ0rzDnqhOZ5O1uQFVOaszEhM3SAASaa9OybbYGLpVQjg'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('ibm')

for tweet in public_tweets:
    print('======================================')
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    print('======================================')


      #class listener(StreamListener):

#	def on_data(self, data):
#		print(data)
#		return true

#	def on_error(self, status):
#		print(status)

#twitterStream = Stream(auth, listener())
#twitterStream.filter([track="dbs"])

"""api = tweepy.API(auth,wait_on_rate_limit=True)
#####United Airlines
# Open/Create a file to append data
csvFile = open('ua.csv', 'a')
#Use csv Writer
csvWriter = csv.writer(csvFile)

for tweet in tweepy.Cursor(api.search,q="dbs bank",lang="en",
                           since="2017-04-03").items():
    print (tweet.created_at, tweet.text)
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])"""