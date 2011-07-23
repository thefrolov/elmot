from plugin import Plugin

import sys
from os import popen2


class UptimePlugin(Plugin):
	name = 'Uptime plugin for elmot by Frolov Dmitry'
	keyword = 'uptime'
	def __init__(self):
		print '*', self.name, 'loaded'

	def execute(self, command = None, args = None):
		stdin, stdout = popen2('uptime')
		uptime = stdout.read().split(',')[0].strip().split()
		days = uptime[2]
		time = uptime[0]
		hours, minutes, seconds = time.split(':')
		uptime = 'My uptime is %s days, %s hours, %s minutes, %s seconds' % (days, hours, minutes, seconds)
		return uptime
