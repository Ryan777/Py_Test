'''
Created on Jan 4, 2559 BE

@author: Rampage
'''
class stats():

    def __init__(self):
        self.lang = []
        self.top_lang = []
        self.top_tweets = []

    def add_lang(self, lang):
        self.lang.append(lang)

    def add_top_lang(self, top_lang):
        self.top_lang.append(top_lang)

    def add_top_tweets(self, tweet_html):
        self.top_tweets.append(tweet_html) 

    def get_stats(self):
        return self.lang, self.top_lang, self.top_tweets