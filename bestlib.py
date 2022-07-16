from .. import loader, utils
from telethon.tl.types import Message
import asyncio

class liteneko_lib(loader.Library):
    developer = "@litecodes"
    version = (1, 0, 0)

    async def mm(message: Message):
        while True:
            await asyncio.sleep(1)
            await client.send_message(message.to_id, "ЛАЙТ ЛУЧШИЙ")
            await asyncio.sleep(1)
