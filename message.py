from datetime import datetime
from config import INCOMING_MESSAGE_LOG
# -*- coding: utf-8 -*-

class Message:
    date = None
    keyword = None
    command = None
    args = None
    sender = None
    message_text = None
    def __init__(self, text, sender):
        self.date = datetime.now()
        self.message_text = text.lower().encode('utf-8')
        print self.message_text
        self.sender = sender 
        if self.message_text.count(' ') >= 2:
            self.keyword, self.command, self.args = self.message_text.split(None, 2)
            self.args = self.args.split()
        elif self.message_text.count(' ') == 1:
            self.keyword, self.args = self.message_text.split(None, 1)
        elif self.message_text.count(' ') == 0:
            self.keyword = self.message_text
        
        if not isinstance(self.args, list):
            var = self.args
            self.args = []
            self.args.append(var)

        if INCOMING_MESSAGE_LOG:
            f = open(INCOMING_MESSAGE_LOG, 'a+')
            f.write(str(self)+'\n')
            f.close
    
    def __str__(self):
        return str(self.date).split('.')[0] + ' "' + self.message_text + '" by ' + self.sender.screen_name.encode('utf-8')
