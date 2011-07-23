class Plugin(object):
	name = 'undefined'
	keyword = 'undefined'
	# actions:
	#  0 - silent
	#  1 - private message
	#  2 - tweet to timeline
	action = 2
	controlled = True
	def __init__(self):
		pass

	def execute(self, cmd, args):
		pass
