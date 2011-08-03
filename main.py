#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pluginmgr import PluginManager
from api import Api
from daemon import Daemon
from message import Message
from config import BASE_PATH, PID_PATH, LOG_PATH, ERROR_LOG_PATH
import sys

sys.path.insert(0, BASE_PATH)

class ElmotDaemon(Daemon):
    def run(self):
        mgr = PluginManager()
        api = Api()
        for mes in api.listenMessages():
            m = Message(mes.text,mes.sender)
            plugin = mgr.getPlugin(m.keyword)

            if plugin.action == 2:
                api.tweet(plugin.execute(m))
            elif plugin.action == 1:
                api.sendDirectMessage(m.sender.id, plugin.execute(m))
            elif plugin.action == 0:
                plugin.execute(m)


if __name__ == "__main__":
    daemon = ElmotDaemon(PID_PATH,'/dev/null', LOG_PATH, ERROR_LOG_PATH)
    if len(sys.argv) == 2:
        if 'start' == sys.argv[1]:
            daemon.start()
        elif 'stop' == sys.argv[1]:
	    daemon.stop()
        elif 'restart' == sys.argv[1]:
            daemon.restart()
        elif 'debug' == sys.argv[1]:
            daemon.run()
        else:
            print "Unknown command"
            sys.exit(2)
    	sys.exit(0)
    else:
        print "usage: %s start|stop|restart|debug" % sys.argv[0]
        sys.exit(2)
