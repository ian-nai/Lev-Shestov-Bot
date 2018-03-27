import nltk
import io
from random import sample
from nltk.tokenize import sent_tokenize
import tweepy
import config
import time

auth = tweepy.OAuthHandler(process.env.CONSUMER_KEY, process.env.CONSUMER_SECRET)
auth.set_access_token(process.env.ACCESS_KEY, process.env.ACCESS_SECRET)
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
