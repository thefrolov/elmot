import os
import pwd
# -*- coding: utf-8 -*-

# Twitter credentials
CONSUMER_KEY = 'TvD4p5rqXlfisqQX7ibvA'
CONSUMER_SECRET = 'oL9FNclaDE2ErL9zTRNZnUiq0GN8afJcmGnJljms'
ACCESS_KEY = '331580893-K22zuD7bqmvNdvdLXM5XuC3jZ8GoGlXZbpWKP6Ss'
ACCESS_SECRET = 'l4jgFBhlHvv5Hy5VyMxAJkmM1RXaJ22JJRUvFe98'

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
