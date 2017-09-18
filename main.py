#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import telepot, time
from EmailConn import EmailChecker
from config import *


#TODO
'''try to reply messages from inbox to telegram
+ add show from

'''

TOKEN = telegram_token
TelegramBot = telepot.Bot(TOKEN)


def handle(msg):

    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)
    command = msg['text'].strip().lower()
    TelegramBot.sendMessage(chat_id, 'Hello')

    if command == '/show':
        with EmailChecker() as emailcheck_obj:
            unreadcount = emailcheck_obj.unread_count()
            bot_msg = ('New mail(s): %s ' % unreadcount)
            TelegramBot.sendMessage(chat_id, bot_msg)

    if command == '/test':
        TelegramBot.sendMessage(chat_id, 'OK')
        print('OK')

    if command == '/stop':
        return 0

    if command == '/show2':
        TelegramBot.sendMessage(chat_id, 'If you want to fetch e-mail messages every hour send me' \
                                         ' /start')

print('Listening..')
TelegramBot.message_loop(handle)

while 1:
    time.sleep(30)