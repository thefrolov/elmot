from plugin import Plugin

import sys
from os import popen2
from api import Api


class RemoveTweetsPlugin(Plugin):
	name = 'Tweets removing plugin for elmot by Frolov Dmitry'
	keyword = 'removetweets'
	action = 0
	def __init__(self):
		print '*', self.name, 'loaded'

	def execute(self, command = None, args = None):
		api = Api()
		for tweet in api.user_timeline(count=args[0]):
			tweet.destroy()
