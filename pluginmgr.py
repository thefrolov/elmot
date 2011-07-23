from plugin import Plugin
from os.path import splitext
from os import listdir
from config import BASE_PATH
import sys

class PluginManager():
	
	plugins = []
				
	def __init__(self):
		ss = listdir(BASE_PATH+'/plugins')
		sys.path.insert(0, BASE_PATH+'/plugins')
	
		for s in ss:
			if (splitext(s)[1] == '.py'):
				__import__(splitext(s)[0], None, None, [''])

		for plugin in Plugin.__subclasses__():
			p = plugin()
			if p.controlled:
				self.plugins.append(p)
			else:
				p.start()
		return

	def getPlugin(self, keyword):
		for plugin in self.plugins:
			if (plugin.keyword == keyword):
				return plugin


