import os
import pwd
# -*- coding: utf-8 -*-

# Twitter credentials
CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_KEY = ''
ACCESS_SECRET = ''

# base path
BASE_PATH = os.path.dirname(__file__)

# pid path
PID_PATH = BASE_PATH+'/elmot.pid'

# people nicknames who can manage system
AUTHORIZED_ACCOUNTS = ['thefrolov']

# logfile
LOG_PATH = BASE_PATH+'/log/elmot.log'
ERROR_LOG_PATH = BASE_PATH+'/log/elmot.err'

# type None to disable incoming message log
INCOMING_MESSAGE_LOG = BASE_PATH+'/log/incoming.log'

# run elmot as user (do not use root)
RUN_UID = pwd.getpwnam("root").pw_uid
