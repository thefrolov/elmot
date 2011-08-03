from plugin import Plugin
import sys
from os import popen2
from api import Api
# -*- coding: utf-8 -*-

class RemoveTweetsPlugin(Plugin):
    name = 'Tweets removing plugin for elmot by Frolov Dmitry'
    keyword = 'removetweets'
    action = 1
    controlled = True    

    def __init__(self):
        Plugin.__init__(self)

    def execute(self, message):
        api = Api()
        counter = 0
        for tweet in api.user_timeline(count=message.args[0]):
            tweet.destroy()
            counter = counter + 1
        return '%i tweets removed' % counter

