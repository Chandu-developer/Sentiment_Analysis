# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 12:46:15 2020

@author: 91779
"""

import csv
from nltk import stopwords
f = open("texts.txt")
x = f.readlines()
s = []

for i in x:
    i = i.replace(","," ")
    j = i.replace(" ",",")
    s.append(j)
print(s)

csvex = csv.writer(open("texts.txt",'w'),delimiter = ',',quoting = csv.QUOTE_ALL)
csvex.writerow(s)

#sentiment ananlysis
import tweepy
from textblob import TextBlob
from nltk.tokenize import TweetTokenizer

#authenticating with twitter
consumer_key = 'YTNePiJ0J4hGv6pkxBdiGEuE5'
consumer_secrect = 'zaQPfFosAZr3IshGsRDqBW3h1AFD7G2Q58Eb4ZwOuwKdBniXo8'
access_token = '1205552450486165504-DGQhnRYR7sTb4E4O1MXK6QnrHsXr0I'
access_token_secrect = 'N1Ex67VyexnvOozGlpIXMqqpzELNbeExphqGblPaKdQef'

auth = tweepy.OAuthHandler(consumer_key,consumer_secrect)
auth.set_access_token(access_token,access_token_secrect)
api = tweepy.API(auth)
public_tweets = api.search('Donald Trump')


for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)