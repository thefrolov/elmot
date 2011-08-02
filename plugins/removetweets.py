from plugin import Plugin
import sys
from os import popen2
from api import Api


class RemoveTweetsPlugin(Plugin):
    name = 'Tweets removing plugin for elmot by Frolov Dmitry'
    keyword = 'removetweets'
    action = 1
    controlled = True    

    def __init__(self):
        Plugin.__init__(self)

    def execute(self, command = None, args = None):
        api = Api()
        counter = 0
        for tweet in api.user_timeline(count=args[0]):
            tweet.destroy()
            counter = counter + 1
        return '%i tweets removed' % counter

