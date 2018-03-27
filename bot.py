import nltk
import io
from random import sample
from nltk.tokenize import sent_tokenize
import tweepy
import config
import time
from boto.s3.connection import S3Connection

s3 = S3Connection(os.environ['CONSUMER_KEY'], os.environ['CONSUMER_SECRET'], os.environ['ACCESS_KEY'], os.environ['ACCESS_SECRET'])

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
