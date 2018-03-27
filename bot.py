import nltk
import os
import io
from random import sample
from nltk.tokenize import sent_tokenize
import tweepy
import time


CONSUMER_KEY = os.environ.get('CONSUMER_KEY') 
CONSUMER_SECRET = os.environ.get('CONSUMER_SECRET')
ACCESS_KEY = os.environ.get('ACCESS_KEY')
ACCESS_SECRET = os.environ.get('ACCESS_SECRET')

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

def sentence_split():
    text1 = "shestov_corpus.txt"
    with io.open(text1, 'r') as file:
        text = file.read()
    sent_text = nltk.sent_tokenize(text) # this gives us a list of sentences

    selected = sample(sent_text, 1)
    tweet =  " ".join(selected)
    return tweet

def wait_function():
    while True:
        tweet = sentence_split()
        api.update_status(tweet)
        time.sleep(21600)

wait_function()
