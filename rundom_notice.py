#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
С 9:30 до 12:00 - 9000 сек; с 13:00 до 15:00 - 7200 сек; с 16:00 до 19:00 - 10800
"""
from random import randint
from time import sleep
from sys import argv
import requests
from os import getenv
from dotenv import load_dotenv

step = argv[1]
token = getenv("token")
chat_id = getenv("chat_id")
message = getenv("message")

def sent_notice(message):
    url = 'https://api.telegram.org/bot' + token + '/sendMessage'
    params = {'chat_id': chat_id, 'text': message}
    requests.post(url, data=params)

if step == '1':
    sleep(randint(0, 9000))
    sent_notice(message)
if step == '2':
    sleep(randint(0, 7200))
    sent_notice(message)
if step == '3':
    sleep(randint(0, 10800))
    sent_notice(message)
