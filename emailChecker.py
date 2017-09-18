#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import imaplib
from config import *

class EmailChecker:
    def __init__(self):
        self.login = email_account
        self.password = email_password
        self.mailbox = imaplib.IMAP4_SSL('outlook.office365.com')
        self.mailbox.login(self.login, self.password)
        self.mailbox.select('INBOX')
        self.result, self.data = self.mailbox.search(None, "ALL")
        print('Connected.')

    def __enter__(self):
        return self

    def unread_count(self):
        ids = self.data[0]  # data is a list.
        id_list = ids.split()  # ids is a space separated string
        print('New mail(s): ', len(id_list))
        return len(id_list)

    def __exit__(self, exc_type, exc_value, traceback):
        self.mailbox.close()
        self.mailbox.logout()