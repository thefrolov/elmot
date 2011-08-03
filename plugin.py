# -*- coding: utf-8 -*-

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
        print '*', self.name, 'loaded'
    
    def execute(self, message):
        pass

    # run method only for non controlled plugins
    # for threading support with python Threads
    def run():
        pass
