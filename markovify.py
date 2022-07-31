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
# @KeyZenD & @D4n13l3k00

#meta developer: @litegay
#requires: markovify aiofiles

import random
from telethon import types
import markovify
from aiofiles import open as aopen
from aiofiles import os as aos
from .. import loader, utils


@loader.tds
class MegaMozgLiteEditionMod(loader.Module):
    strings = {
        'name': 'MegaMozgLiteEdition',
        'pref': '<b>[MegaMozgLiteEdition]</b> ',
        'need_arg': '{}Нужен аргумент',
        'status': '{}{}',
        'on': '{}Включён',
        'off': '{}Выключен',
        
    }
    _db_name = 'MegaMozgLiteEdition'

    async def client_ready(self, client, db):
        self.db = db
        self.client = client
    
    @staticmethod
    def str2bool(v):
        return v.lower() in ("yes", "y", "ye", "yea", "true", "t", "1", "on", "enable", "start", "run", "go", "да")

    
    async def mozgcmd(self, m: types.Message):
        '.mozgle <on/off/...> - Переключить режим дурачка в чате'
        args = utils.get_args_raw(m)
        if not m.chat:
            return
        chat = m.chat.id
        if self.str2bool(args):
            chats: list = self.db.get(self._db_name, 'chats', [])
            chats.append(chat)
            chats = list(set(chats))
            self.db.set(self._db_name, 'chats', chats)
            return await utils.answer(m, self.strings('on').format(self.strings('pref')))
        chats: list = self.db.get(self._db_name, 'chats', [])
        try:
            chats.remove(chat)
        except:
            pass
        chats = list(set(chats))
        self.db.set(self._db_name, 'chats', chats)
        return await utils.answer(m, self.strings('off').format(self.strings('pref')))

    async def mozgchancelecmd(self, m: types.Message):
        '.mozgchance <int> - Устанвоить шанс 1 к N.\n0 - всегда отвечать'
        args: str = utils.get_args_raw(m)
        if args.isdigit():
            self.db.set(self._db_name, 'chance', int(args))
            return await utils.answer(m, self.strings('status').format(self.strings('pref'), args))
            
        return await utils.answer(m, self.strings('need_arg').format(self.strings('pref')))
    
    async def watcher(self, m: types.Message):
        if not isinstance(m, types.Message):
            return
        if m.sender_id == (await m.client.get_me()).id or not m.chat:
            return
        if m.chat.id not in self.db.get(self._db_name, 'chats', []):
            return
        ch = self.db.get(self._db_name, 'chance', 0)
        if ch != 0:
            if random.randint(0, ch) != 0:
                return
        try:
            text = m.raw_text
            file_name = f"megamozgle-{m.peer_id}"
            async with aopen(file_name, "a", encoding="utf-8") as f:
                await f.write(f"\n{text}")
        except Exception:
            return
        async with aopen(file_name, encoding="utf-8") as f:
            db = await f.read()
        db = db.strip().lower()
        text_model = markovify.NewlineText(
            input_text=db, state_size=1, well_formed=False
        )
        sentence = text_model.make_sentence(tries=1000) or random.choice(
            db.splitlines()
        )
        await self.client.send_message(m.to_id, sentence)