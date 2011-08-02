#!/usr/bin/env python

from pluginmgr import PluginManager
from api import Api
from daemon import Daemon
from config import BASE_PATH, PID_PATH, LOG_PATH, ERROR_LOG_PATH
import sys

sys.path.insert(0, BASE_PATH)

class ElmotDaemon(Daemon):
    def run(self):
        mgr = PluginManager()
        api = Api()
        for mes in api.listenMessages():
            if mes.text.count(' ') >= 2:
                keyword, command, args = mes.text.split(None, 2)
	        args = args.split()
            elif mes.text.count(' ') == 1:
                keyword, args = mes.text.split(None, 1)
                args = args.split()
                command = None
            elif mes.text.count(' ') == 0:
                keyword = mes.text
                command = None
                args = None
            plugin = mgr.getPlugin(keyword)
            if plugin.action == 2:
                api.tweet(plugin.execute(command,args))
            elif plugin.action == 1:
                api.sendDirectMessage(mes.sender.id,plugin.execute(command,args))
            elif plugin.action == 0:
                plugin.execute(command,args)


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
