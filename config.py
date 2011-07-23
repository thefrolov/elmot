import os
import pwd
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
AUTHORIZED_ACCOUNTS = ['']

# logfile
LOG_PATH = BASE_PATH+'/elmot.log'

# run elmot as user (do not use root)
RUN_UID = pwd.getpwnam("root").pw_uid
