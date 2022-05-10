#meta developer: @yaroslav1734
#scope: inline

import time
import logging

from .. import loader, utils
from ..inline.types import InlineQuery

class InlinePingMod (loader.Module):
    """Инлайн пинг"""
    strings = {
        "name": "Inline ping",
        "results_ping": "⏱ <b>Response time:</b> <code>{}</code> <b>ms</b>\n👩‍💼 <b>Uptime: {}</b>",
    }

    strings_ru = {
        "results_ping": "⏱ <b>Скорость отклика:</b> <code>{}</code> <b>ms</b>\n👩‍💼 <b>Прошло с последней перезагрузки: {}</b>"
    }


    async def ping_inline_handler(self, query: InlineQuery):
        """Test your userbot ping"""
        start = time.perf_counter_ns()
        result = self.strings("results_ping").format(
                round((time.perf_counter_ns() - start) / 10**6, 3),
                utils.formatted_uptime(),
            )
        return {
            "title": "Узнать пинг",
            "description": "Ну жми...",
            "thumb": "https://st.depositphotos.com/1031174/3569/i/950/depositphotos_35699393-stock-photo-clock.jpg",
            "message": result,
        }
