#!/usr/bin/env python3
import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
import fileinput
import re
from nltk.corpus import stopwords
import os


consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

e = set(stopwords.words('english'))

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


def process(tweet):
    with open('tweetwords.txt', 'w', encoding='utf-8') as f:
        for i in tweet:
            print(i.text.encode("utf-8"))
            f.write(str(i.text.encode("utf-8")))
            f.write('\n')

    f.close()
    clean()


def clean():
    with open('tweetwords.txt', 'r', encoding='utf-8') as f2:
        with open('tweetwords2.txt', 'w', encoding='utf-8') as f3:
            words_seen = set()
            for line in f2:
                s = re.sub(r'http.*|\\x.*|@|b\'|#|\\n|\/s|\.|\"|\:|!|\?|\'|,|&amp;|', "", line)  # regex to remove jibberish
                for word in filter(lambda w: w.lower() not in e, s.split()):  # nltk processing to remove common words
                    if word.lower() not in words_seen:
                        f3.write(word.lower())
                        print(word.lower())
                        f3.write('\n')
                        words_seen.add(word.lower())
    genpass()
                        
               

    f2.close()
    f3.close()


def genpass():
    os.system('john --wordlist=./tweetwords2.txt --stdout --rules:modified_single > ./tweet_pass.txt')
   


def main():

    target = input('Enter the Twitter ID:')
    get_tweets(target)


def get_tweets(uname):

    alltweets = []
    newtweets = api.user_timeline(screen_name=uname, count=200)
    alltweets.extend(newtweets)
    tweetid = alltweets[-1].id - 1

    while len(newtweets) > 0:
        print('Geting tweet before:{}'.format(tweetid))
        newtweets = api.user_timeline(screen_name=uname, count=200, max_id=tweetid)
        alltweets.extend(newtweets)
        tweetid = alltweets[-1].id - 1
        # print(alltweets.text.encode("utf-8"))
        print('Tweet Downloaded:{}'.format(len(alltweets)))

    process(alltweets)


if __name__ == '__main__':
    main()
