# -*- coding: utf-8 -*-
import sys
import time
from threading import Thread
from api import Api
from plugin import Plugin
import socket
from datetime import datetime

# map of server with true flag
# format:
# [ip, port, True]

SERVERS = [
    ['10.2.3.3', 22, True],
    ['8.8.8.8', 53, True]
    ]

class ConnTestPlugin(Plugin, Thread):
    name = 'Connectivity test plugin for elmot by Frolov Dmitry'
    keyword = 'conntest'
    controlled = False
    def __init__(self):
        Plugin.__init__(self)
        Thread.__init__(self)
        self.api = Api()
	
    def check(self,remote_host,remote_port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(10)
        try:
            sock.connect((remote_host, remote_port))
            return True
        except Exception,ex:
            print ex
            return False
        sock.close()

    def run(self, message = None):
        while True:
            for server in SERVERS:
                if not self.check(server[0], server[1]):
                    if server[2]:
                        self.api.tweet(str(datetime.now()).split('.')[0] + ' connection lost with ' + server[0])
                        server[2] = False
                else:
                    if not server[2]:
                        self.api.tweet(str(datetime.now()).split('.')[0] + ' connection established with ' + server[0])
                        server[2] = True
			
            time.sleep(30)
