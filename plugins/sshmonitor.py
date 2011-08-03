# -*- coding: utf-8 -*-
import sys
import time
from threading import Thread
from api import Api
from plugin import Plugin
class SshMonitorPlugin(Plugin, Thread):
    name = 'ssh monitoring plugin for elmot by Frolov Dmitry'
    keyword = 'sshmon'
    controlled = False
    
    def __init__(self):
        Plugin.__init__(self)
        Thread.__init__(self)
        self.api = Api()
	
    def follow(self, thefile):
        thefile.seek(0,2)
        while True:
            line = thefile.readline()
            if not line:
                time.sleep(0.1)
                continue
            if ('Failed password' in line):
                yield line.split(': ')[1].split('port')[0]


    def run(self):
        logfile = open('/var/log/auth.log')
        loglines = self.follow(logfile)
        
        for line in loglines:
            line = line.replace('invalid user ', '', 1)
            self.api.tweet(line)
