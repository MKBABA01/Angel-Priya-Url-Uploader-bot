#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Thank you @LazyDeveloperr 

# the logging things
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os

# the secret configuration specific things
if bool(os.environ.get("WEBHOOK", 'true'):
    from sample_config import Config
else:
    from config import Config

import pyrogram
logging.getLogger("pyrogram").setLevel(logging.WARNING)


if __name__ == "__main__" :
    # create download directory, if not exist
    if not os.path.isdir(Config.DOWNLOAD_LOCATION):
        os.makedirs(Config.DOWNLOAD_LOCATION)
    plugins = dict(
        root="plugins"
    )
    app = pyrogram.Client(
        "BewafaAngelPriya",
        bot_token=Config.TG_BOT_TOKEN, "5993061070:AAGuC4I62mPia3GzGBtz4qbeQl5H2pAmyE4"
        api_id=Config.APP_ID, "20886519"
        api_hash=Config.API_HASH, "200096623fc84f791d07d8b44169b163"
        plugins=plugins
    )
    Config.AUTH_USERS.add(5497597228)
    app.run()
