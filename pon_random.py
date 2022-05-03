__version__ = (1, 0, 2)
#meta developer: @yaroslav1734
#scope: inline
#scope: hikka_only

import random
import logging
from ..inline.types import InlineQuery
from .. import loader, utils
import asyncio
from telethon.tl.types import Message

logger = logging.getLogger(__name__)

@loader.tds
class InlineRandomMod(loader.Module):
    """Твой рандомный пон"""
    strings = {
        'name': 'InlinePon'
    }

    @loader.inline_everyone
    async def pon_inline_handler(self, query: InlineQuery):
        """Случайный пон"""

        pon = random.choice(["страшный", "интересный", "уютный", "любопытный", "афигенный", "весёлый", "крутой", "злой", "лютый", "странный"])

        return {
            "title": "Твой пон на сегодня",
            "description": "Итак...",
            "message": f"<i>Силы пона говорят что твой пон на сегодня:</i> <b>{pon} пон</b>"
        }