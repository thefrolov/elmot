# -*- coding: utf-8 -*-
from plugin import Plugin
import sys
from os import popen2
from api import Api

# plugin for override unknown action
class RemoveTweetsPlugin(Plugin):
    name = 'default plugin for elmot by Frolov Dmitry'
    keyword = 'default'
    action = 1
    controlled = True    

    def __init__(self):
        Plugin.__init__(self)

    def execute(self, message):
        return 'unknown message "%s"' % message.message_text
