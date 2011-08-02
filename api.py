import tweepy
import sys, time
from config import *


class Api:
    class __impl:
        user_timeline = None
        
        def __init__(self):
            self.auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
            self.auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
            self.api = tweepy.API(self.auth)
            self.user_timeline = self.api.user_timeline

        def tweet(self, text):
            try:
                self.api.update_status(text)
            except Exception, ex:
                print ex
            
        def sendDirectMessage(self,userid, msg):
            try:
                self.api.send_direct_message(user = userid, text = msg)
            except Exception, ex:
                print ex
           
        def listenMessages(self):
            while True:
                try:
                    msg = self.api.direct_messages()[0]
                except Exception, ex:
                    time.sleep(30)
                    continue
                msg = msg.destroy()
                if msg.sender.screen_name in AUTHORIZED_ACCOUNTS:
                    yield msg

        def removeTweets(self, num):
            for tweet in self.api.user_timeline(count=num):
                tweet.destroy()


    __instance = None
    
    def __init__(self):
        if Api.__instance is None:
            Api.__instance = Api.__impl()
            self.__dict__['_Api__instance'] = Api.__instance
    
    def __getattr__(self, attr):
        return getattr(self.__instance, attr)

    def __setattr__(self, attr, value):
        return setattr(self.__instance, attr, value)
