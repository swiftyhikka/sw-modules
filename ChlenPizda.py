__version__ = (1, 0, 0)
#meta developer: @wr1te_code
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
    """Твой рандомный писюн в ротик"""
    strings = {
        'name': 'ChlenPizda'
    }

    @loader.inline_everyone
    async def hui_inline_handler(self, query: InlineQuery):
        """Дилдо размером с мамой твоей"""

        huila = random.choice(["тупой долбаеб", "хиракири", "вася 228", "майнкрафтер", "школа номер 8", "ебашишь героин", "крутой", "моча армянская", "сперма отчима", "павел дуров (легендарка✨)"])
        haha = random.choice(["вагины", "спермы", "члена", "клитора"])

        return {
            "title": "Пиздак затянул, или я те ебало сломаю.",
            "description": "Иди нахуй пжж...",
            "message": f"<i>🥶 Силы {haha} говорят что ты сегодня:</i> <b>{huila}.</b>"
        }