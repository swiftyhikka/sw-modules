from .. import loader
from asyncio import sleep
#meta developer: @wr1te_code

@loader.tds
class AnimSmiles(loader.Module):
    strings = {"name": "AnimatedSmiles"}

    @loader.owner
    async def dizlikecmd(self, message):
        for _ in range(1):
            for dizlike in ["🟥🟥🟥🟥🟥🟥🟥🟥", "🟥🟥🟥🟥🟥🟥🟥🟥\n🟥🟥⬜⬜⬜🟥⬜🟥", "🟥🟥🟥🟥🟥🟥🟥🟥\n🟥🟥⬜⬜⬜🟥⬜🟥\n🟥🟥⬜⬜⬜🟥⬜🟥", "🟥🟥🟥🟥🟥🟥🟥🟥\n🟥🟥⬜⬜⬜🟥⬜🟥\n🟥🟥⬜⬜⬜🟥⬜🟥\n🟥⬜⬜⬜⬜🟥⬜🟥", "🟥🟥🟥🟥🟥🟥🟥🟥\n🟥🟥⬜⬜⬜🟥⬜🟥\n🟥🟥⬜⬜⬜🟥⬜🟥\n🟥⬜⬜⬜⬜🟥⬜🟥\n🟥🟥🟥🟥⬜🟥⬜🟥", "🟥🟥🟥🟥🟥🟥🟥🟥\n🟥🟥⬜⬜⬜🟥⬜🟥\n🟥🟥⬜⬜⬜🟥⬜🟥\n🟥⬜⬜⬜⬜🟥⬜🟥\n🟥🟥🟥🟥⬜🟥⬜🟥\n🟥🟥🟥🟥🟥🟥🟥🟥"]:
                await message.edit(dizlike)
                await sleep(0.5)
    async def likecmd(self, message):
       for _ in range(1):
            for like in ["🟦🟦🟦🟦🟦🟦🟦🟦", "🟦🟦🟦🟦🟦🟦🟦🟦\n🟦🟦🟦🟦⬜🟦⬜🟦", "🟦🟦🟦🟦🟦🟦🟦🟦\n🟦🟦🟦🟦⬜🟦⬜🟦\n🟦⬜⬜⬜⬜🟦⬜🟦", "🟦🟦🟦🟦🟦🟦🟦🟦\n🟦🟦🟦🟦⬜🟦⬜🟦\n🟦⬜⬜⬜⬜🟦⬜🟦\n🟦🟦⬜⬜⬜🟦⬜🟦", "🟦🟦🟦🟦🟦🟦🟦🟦\n🟦🟦🟦🟦⬜🟦⬜🟦\n🟦⬜⬜⬜⬜🟦⬜🟦\n🟦🟦⬜⬜⬜🟦⬜🟦\n🟦🟦⬜⬜⬜🟦⬜🟦", "🟦🟦🟦🟦🟦🟦🟦🟦\n🟦🟦🟦🟦⬜🟦⬜🟦\n🟦⬜⬜⬜⬜🟦⬜🟦\n🟦🟦⬜⬜⬜🟦⬜🟦\n🟦🟦⬜⬜⬜🟦⬜🟦\n🟦🟦🟦🟦🟦🟦🟦🟦"]:
                await message.edit(like)
                await sleep(0.5)
    async def pornhubcmd(self, message):
       for _ in range(1):
            for pornhub in ["⬛⬛⬛⬛⬛⬛⬛⬛⬛", "⬛⬛⬛⬛⬛⬛⬛⬛⬛\n⬛🟧🟧🟧⬛🟧⬛🟧⬛", "⬛⬛⬛⬛⬛⬛⬛⬛⬛\n⬛🟧🟧🟧⬛🟧⬛🟧⬛\n⬛🟧⬛🟧⬛🟧⬛🟧⬛","⬛⬛⬛⬛⬛⬛⬛⬛⬛\n⬛🟧🟧🟧⬛🟧⬛🟧⬛\n⬛🟧⬛🟧⬛🟧⬛🟧⬛\n⬛🟧🟧🟧⬛🟧🟧🟧⬛", "⬛⬛⬛⬛⬛⬛⬛⬛⬛\n⬛🟧🟧🟧⬛🟧⬛🟧⬛\n⬛🟧⬛🟧⬛🟧⬛🟧⬛\n⬛🟧🟧🟧⬛🟧🟧🟧⬛\n⬛🟧⬛⬛⬛🟧⬛🟧⬛", "⬛⬛⬛⬛⬛⬛⬛⬛⬛\n⬛🟧🟧🟧⬛🟧⬛🟧⬛\n⬛🟧⬛🟧⬛🟧⬛🟧⬛\n⬛🟧🟧🟧⬛🟧🟧🟧⬛\n⬛🟧⬛⬛⬛🟧⬛🟧⬛\n⬛🟧⬛⬛⬛🟧⬛🟧⬛", "⬛⬛⬛⬛⬛⬛⬛⬛⬛\n⬛🟧🟧🟧⬛🟧⬛🟧⬛\n⬛🟧⬛🟧⬛🟧⬛🟧⬛\n⬛🟧🟧🟧⬛🟧🟧🟧⬛\n⬛🟧⬛⬛⬛🟧⬛🟧⬛\n⬛🟧⬛⬛⬛🟧⬛🟧⬛\n⬛⬛⬛⬛⬛⬛⬛⬛⬛"]:
                await message.edit(pornhub)
                await sleep(0.5)
    async def smilecmd(self, message):
       for _ in range(1):
            for smile in ["⬛⬛⬛⬛⬛⬛⬛ ", "⬛⬛⬛⬛⬛⬛⬛\n⬛⬜⬛⬛⬛⬜⬛", "⬛⬛⬛⬛⬛⬛⬛\n⬛⬜⬛⬛⬛⬜⬛\n⬛⬛⬛⬛⬛⬛⬛", "⬛⬛⬛⬛⬛⬛⬛\n⬛⬜⬛⬛⬛⬜⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬜⬛⬛⬛⬜⬛", "⬛⬛⬛⬛⬛⬛⬛\n⬛⬜⬛⬛⬛⬜⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬜⬛⬛⬛⬜⬛\n⬛⬛⬜⬜⬜⬛⬛", "⬛⬛⬛⬛⬛⬛⬛\n⬛⬜⬛⬛⬛⬜⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬜⬛⬛⬛⬜⬛\n⬛⬛⬜⬜⬜⬛⬛\n⬛⬛⬛⬛⬛⬛⬛"]:
                await message.edit(smile)
                await sleep(0.3)
    async def bibliyacmd(self, message):
       for _ in range(1):
            for bibliya in ["⬜⬜⬜⬜⬜", "⬜⬜⬜⬜⬜\n⬜⬜🟨⬜⬜", "⬜⬜⬜⬜⬜\n⬜⬜🟨⬜⬜\n⬜🟨🟨🟨⬜", "⬜⬜⬜⬜⬜\n⬜⬜🟨⬜⬜\n⬜🟨🟨🟨⬜\n⬜⬜🟨⬜⬜", "⬜⬜⬜⬜⬜\n⬜⬜🟨⬜⬜\n⬜🟨🟨🟨⬜\n⬜⬜🟨⬜⬜\n⬜⬜🟨⬜⬜", "⬜⬜⬜⬜⬜\n⬜⬜🟨⬜⬜\n⬜🟨🟨🟨⬜\n⬜⬜🟨⬜⬜\n⬜⬜🟨⬜⬜\n⬜⬜⬜⬜⬜"]:
                await message.edit(bibliya)
                await sleep(0.3)