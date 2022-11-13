from .. import loader, utils

import logging
import datetime
import time
import telethon

from telethon import types
from telethon.tl.types import Message

logger = logging.getLogger(__name__)

class heal():
    async def heal(self, message):
        if message.raw_text == 'хил':
            message.reply('!купить вакцину')
