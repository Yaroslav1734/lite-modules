"""Модуль для поиска уровней"""
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
#meta developer: @iamliterally9yo
#scope: hikka_only
#requires: GDBrowserPy
from logging import exception
from .. import loader, utils
from ..inline.types import InlineCall
from telethon.tl.types import Message
from GDBrowserPy import GD

@loader.tds
class GDMenuMod(loader.Module):
    """Модуль для поиска уровней в гд"""

    strings = {
        "name": "GDMenu",
        "level_not_exists": "❌Данного уровня не существует!",
        "not_int": "❌Нужно указать айди уровня!",
        "succ": "<b>Название: </b><code>{}</code>\n<b>Айди: </b><code>{}</code>\n<b>Создатель: </b><code>{}</code>\n<b>Сложность: </b><code>{}</code>\n<b>Описание: </b><code>{}</code>",
        "_cfg_login": "Логин от аккаунта",
        "_cfg_password": "Пароль от аккаунта"
    }

    async def client_ready(self, client, db):
        self.client = client
        self.db = db

    async def searchlvlcmd(self, message: Message):
        """В аргументах укажи айди уровня!"""
        args = utils.get_args(message)
        if len(args) == 0:
            await message.edit(self.strings("not_int"))
        else:
            try:
                lvl_id = args[0]
                lvl = GD.Level(id=lvl_id, download=False)
                await message.edit(self.strings("succ").format(
                    lvl.name,
                    lvl.id,
                    lvl.author,
                    lvl.difficultyFace,
                    lvl.description,
                ),
                )
            except exception:
                await message.edit(self.strings("level_not_exists"))
