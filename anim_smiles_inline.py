from .. import loader, utils
from asyncio import sleep
#meta developer: @wr1te_code | @anon97945

@loader.tds
class AnimSmiles(loader.Module):
    strings = {"name": "AnimatedSmiles"}

    @loader.owner
    async def dizlikecmd(self, message):
        dizlike = []
        for _ in range(1):
            inline_msg = await self.inline.form(message=message, text="⁭⁫⁪⁫⁬⁭⁫🟥🟥🟥🟥🟥🟥🟥🟥", reply_markup={"text": "\u0020\u2800", "data": "empty"})
            for dizlike in ["🟥🟥🟥🟥🟥🟥🟥🟥\n🟥🟥⬜⬜⬜🟥⬜🟥", "🟥🟥🟥🟥🟥🟥🟥🟥\n🟥🟥⬜⬜⬜🟥⬜🟥\n🟥🟥⬜⬜⬜🟥⬜🟥", "🟥🟥🟥🟥🟥🟥🟥🟥\n🟥🟥⬜⬜⬜🟥⬜🟥\n🟥🟥⬜⬜⬜🟥⬜🟥\n🟥⬜⬜⬜⬜🟥⬜🟥", "🟥🟥🟥🟥🟥🟥🟥🟥\n🟥🟥⬜⬜⬜🟥⬜🟥\n🟥🟥⬜⬜⬜🟥⬜🟥\n🟥⬜⬜⬜⬜🟥⬜🟥\n🟥🟥🟥🟥⬜🟥⬜🟥", "🟥🟥🟥🟥🟥🟥🟥🟥\n🟥🟥⬜⬜⬜🟥⬜🟥\n🟥🟥⬜⬜⬜🟥⬜🟥\n🟥⬜⬜⬜⬜🟥⬜🟥\n🟥🟥🟥🟥⬜🟥⬜🟥\n🟥🟥🟥🟥🟥🟥🟥🟥"]:
                inline_msg = await utils.answer(inline_msg, dizlike)
                await sleep(1)
    async def likecmd(self, message):
        likecmd = []
        for _ in range(1):
            inline_msg = await self.inline.form(message=message, text="⁭⁫⁪⁫⁬⁭⁫⁪🟦🟦🟦🟦🟦🟦🟦🟦⁭⁫⁪⁫⁬⁭⁫⁪⁫⁬", reply_markup={"text": "\u0020\u2800", "data": "empty"})
            for like in ["🟦🟦🟦🟦🟦🟦🟦🟦\n🟦🟦🟦🟦⬜🟦⬜🟦", "🟦🟦🟦🟦🟦🟦🟦🟦\n🟦🟦🟦🟦⬜🟦⬜🟦\n🟦⬜⬜⬜⬜🟦⬜🟦", "🟦🟦🟦🟦🟦🟦🟦🟦\n🟦🟦🟦🟦⬜🟦⬜🟦\n🟦⬜⬜⬜⬜🟦⬜🟦\n🟦🟦⬜⬜⬜🟦⬜🟦", "🟦🟦🟦🟦🟦🟦🟦🟦\n🟦🟦🟦🟦⬜🟦⬜🟦\n🟦⬜⬜⬜⬜🟦⬜🟦\n🟦🟦⬜⬜⬜🟦⬜🟦\n🟦🟦⬜⬜⬜🟦⬜🟦", "🟦🟦🟦🟦🟦🟦🟦🟦\n🟦🟦🟦🟦⬜🟦⬜🟦\n🟦⬜⬜⬜⬜🟦⬜🟦\n🟦🟦⬜⬜⬜🟦⬜🟦\n🟦🟦⬜⬜⬜🟦⬜🟦\n🟦🟦🟦🟦🟦🟦🟦🟦"]:
                inline_msg = await utils.answer(inline_msg, like)
                await sleep(0.5)
    async def pornhubcmd(self, message):
        pornhubcmd = []
        for _ in range(1):
            inline_msg = await self.inline.form(message=message, text="⬛⬛⬛⬛⬛⬛⬛⬛⬛⁭⁫⁪⁫⁬⁭⁫⁪⁫⁬", reply_markup={"text": "\u0020\u2800", "data": "empty"})
            for pornhub in ["⬛⬛⬛⬛⬛⬛⬛⬛⬛\n⬛🟧🟧🟧⬛🟧⬛🟧⬛", "⬛⬛⬛⬛⬛⬛⬛⬛⬛\n⬛🟧🟧🟧⬛🟧⬛🟧⬛\n⬛🟧⬛🟧⬛🟧⬛🟧⬛","⬛⬛⬛⬛⬛⬛⬛⬛⬛\n⬛🟧🟧🟧⬛🟧⬛🟧⬛\n⬛🟧⬛🟧⬛🟧⬛🟧⬛\n⬛🟧🟧🟧⬛🟧🟧🟧⬛", "⬛⬛⬛⬛⬛⬛⬛⬛⬛\n⬛🟧🟧🟧⬛🟧⬛🟧⬛\n⬛🟧⬛🟧⬛🟧⬛🟧⬛\n⬛🟧🟧🟧⬛🟧🟧🟧⬛\n⬛🟧⬛⬛⬛🟧⬛🟧⬛", "⬛⬛⬛⬛⬛⬛⬛⬛⬛\n⬛🟧🟧🟧⬛🟧⬛🟧⬛\n⬛🟧⬛🟧⬛🟧⬛🟧⬛\n⬛🟧🟧🟧⬛🟧🟧🟧⬛\n⬛🟧⬛⬛⬛🟧⬛🟧⬛\n⬛🟧⬛⬛⬛🟧⬛🟧⬛", "⬛⬛⬛⬛⬛⬛⬛⬛⬛\n⬛🟧🟧🟧⬛🟧⬛🟧⬛\n⬛🟧⬛🟧⬛🟧⬛🟧⬛\n⬛🟧🟧🟧⬛🟧🟧🟧⬛\n⬛🟧⬛⬛⬛🟧⬛🟧⬛\n⬛🟧⬛⬛⬛🟧⬛🟧⬛\n⬛⬛⬛⬛⬛⬛⬛⬛⬛"]:
                inline_msg = await utils.answer(inline_msg, pornhub)
                await sleep(1)
    async def smilecmd(self, message):
        smile = []
        for _ in range(1):
            inline_msg = await self.inline.form(message=message, text="⬛⬛⬛⬛⬛⬛⬛⁭⁫⁪⁫⁬⁭⁫⁪⁫⁬", reply_markup={"text": "\u0020\u2800", "data": "empty"})
            for smile in ["⬛⬛⬛⬛⬛⬛⬛\n⬛⬜⬛⬛⬛⬜⬛", "⬛⬛⬛⬛⬛⬛⬛\n⬛⬜⬛⬛⬛⬜⬛\n⬛⬛⬛⬛⬛⬛⬛", "⬛⬛⬛⬛⬛⬛⬛\n⬛⬜⬛⬛⬛⬜⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬜⬛⬛⬛⬜⬛", "⬛⬛⬛⬛⬛⬛⬛\n⬛⬜⬛⬛⬛⬜⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬜⬛⬛⬛⬜⬛\n⬛⬛⬜⬜⬜⬛⬛", "⬛⬛⬛⬛⬛⬛⬛\n⬛⬜⬛⬛⬛⬜⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬜⬛⬛⬛⬜⬛\n⬛⬛⬜⬜⬜⬛⬛\n⬛⬛⬛⬛⬛⬛⬛"]:
                inline_msg = await utils.answer(inline_msg, smile)
                await sleep(1)
    async def bibliyacmd(self, message):
        bibliyacmd = []
        for _ in range(1):
            inline_msg = await self.inline.form(message=message, text="⁭⁫⁪⁫⁬⁭⁫⁪⬜⬜⬜⬜⬜⁭⁫⁪⁫⁬⁭⁫⁪⁫⁬", reply_markup={"text": "\u0020\u2800", "data": "empty"})
            for bibliya in ["⬜⬜⬜⬜⬜\n⬜⬜🟨⬜⬜", "⬜⬜⬜⬜⬜\n⬜⬜🟨⬜⬜\n⬜🟨🟨🟨⬜", "⬜⬜⬜⬜⬜\n⬜⬜🟨⬜⬜\n⬜🟨🟨🟨⬜\n⬜⬜🟨⬜⬜", "⬜⬜⬜⬜⬜\n⬜⬜🟨⬜⬜\n⬜🟨🟨🟨⬜\n⬜⬜🟨⬜⬜\n⬜⬜🟨⬜⬜", "⬜⬜⬜⬜⬜\n⬜⬜🟨⬜⬜\n⬜🟨🟨🟨⬜\n⬜⬜🟨⬜⬜\n⬜⬜🟨⬜⬜\n⬜⬜⬜⬜⬜"]:
                inline_msg = await utils.answer(inline_msg, bibliya)
                await sleep(1)