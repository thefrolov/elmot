from plugin import Plugin

import sys
from os import popen2


class UptimePlugin(Plugin):
	name = 'Uptime plugin for elmot by Frolov Dmitry'
	keyword = 'uptime'
	def __init__(self):
		print '*', self.name, 'loaded'

	def execute(self, command = None, args = None):
		f = open('/proc/uptime')
		seconds = int(f.read().split()[0].split('.')[0])
		f.close()
		minutes, seconds = divmod(seconds, 60)
		hours, minutes = divmod(minutes, 60)
		days, hours = divmod(hours, 24)
		uptime = 'My uptime is %s days, %s hours, %s minutes, %s seconds' % (days, hours, minutes, seconds)
		return uptime
