# OSINT_tweets
OSINT_tweets- Open Source Intelligence Tool for tweets. Tool that can gather tweets for passive recon and password profiling 
# Synopsis
Passive Reconnaissance is one of the most powerful and underestimated methods of knowing the target. This tool simply uses twitter's API to gather all the tweets of a user and make a clean wordlist out of it, filtering out all the stopwords. This word list is then fed to the "John The Ripper(JTR)" tool to create a custom password dictionary based on "Korelogic" rules. 
The custom password dictionary created would be specific to the user/target.

John the ripper:https://github.com/magnumripper/JohnTheRipper
Korelogic:http://contest-2010.korelogic.com/rules.html 

# Motivation
 The most common form of authentication is the combination of a username and a password or passphrase. It is crucial to use difficult passwords to increase password strength. A weak password can also be one that is easily guessed by someone profiling the user on social media and gathering the common words used by a user.  It can be used in situations like legal penetration tests or forensic crime investigations

# Installation Requirements:
Python3
John the Ripper: Follow instructions on https://github.com/magnumripper/JohnTheRipper
Korelogic Rules: Follow instructions on http://contest-2010.korelogic.com/rules.html
Python Libraries: tweepy, re, nltk.corpus, os
Twitter API Keys: Follow instructions on https://dev.twitter.com/oauth/overview
Edit the tweetpass.py and add you twitter API keys

# API Reference:
Follow instructions on https://dev.twitter.com/oauth/overview

# Tests:
root@kali:~/Desktop/tweet_project# ./tweetpaas2.py 
Enter the Twitter ID: <enter the twitter handle>

# Disclaimer:
The tool is intended for educational purposes only. I do not assume any responsibility for the tool. Use this material at your own discretion and with proper authorization. 




