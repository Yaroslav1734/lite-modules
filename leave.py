#
#   ██╗░░░░░██╗████████╗███████╗░░░░░░
#   ██║░░░░░██║╚══██╔══╝██╔════╝░░░░░░
#   ██║░░░░░██║░░░██║░░░█████╗░░░░░░░░
#   ██║░░░░░██║░░░██║░░░██╔══╝░░░░░░░░
#   ███████╗██║░░░██║░░░███████╗██╗██╗
#   ╚══════╝╚═╝░░░╚═╝░░░╚══════╝╚═╝╚═╝
#
#              © Copyright 2022
#
#          https://t.me/litecodes
#
#         Licensed under the GNU GPLv3
#    https://www.gnu.org/licenses/agpl-3.0.html
#meta developer: @litecodes
#scope: hikka_only
from .. import loader, utils
from telethon.tl.functions.channels import LeaveChannelRequest
from telethon.tl.types import Message
from asyncio import sleep

class LeaveMod(loader.Module):
    strings = {
        "name": "iLeave",
        "_cfg_leave_seconds": "Модуль покинет чат через указанное количество секунд",
        "leavetext": "Текст после которого юзербот покинет чат"
    }

    def __init__(self):
        self._ratelimit = []
        self.config = loader.ModuleConfig(
            loader.ConfigValue(
                "leavetext",
                "<b>Я ливаю</b>",
                doc=lambda: self.strings("leavetext"),
            ),
        )

    async def leavecmd(self, message: Message):
        """Покидает чат в котором ты напишешь команду!"""
        
        if not message.is_private:
            await message.edit(self.config["leavetext"])
            await sleep(1)
            await message.client(LeaveChannelRequest(message.to_id))
        else:
            await message.edit("<b>Я не смог ливнуть из тимы раков :(</b>")