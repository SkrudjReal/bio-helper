from .. import loader, utils

import logging
import datetime
import time

from telethon import types
from telethon import eventsi

logger = logging.getLogger(__name__)

class heal():
    if message.raw_text == 'хил':
        message.reply('!купить вакцину')
