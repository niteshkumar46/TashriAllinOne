#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6482592579:AAG-7yfQX9SjLg1NllouDQ1RDJE5fk2XUlQQ")
    API_ID = int(os.environ.get("API_ID", "28471045"))
    API_HASH = os.environ.get("API_HASH", "040e6f526cdc04260390867ffa01c442")
    AUTH_USERS = "6126200262"

