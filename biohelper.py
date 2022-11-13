from .. import loader, utils

import logging
import datetime
import time
import telethon

from telethon import types
from telethon.tl.types import Message

logger = logging.getLogger(__name__)

@loader.tds
class heal(loader.Module):
    
    def __init__(self):
        self.config = loader.ModuleConfig("POSSIBLE_VALUES", {"хил - .купить вакцину")

    
    async def heal(self, message):
        if await self.allmodules.check_security(message, security.OWNER | security.SUDO):
            args = utils.get_args(message)
            if message.raw_text == 'хил':
                print(message)
                message.reply('.купить вакцину')
