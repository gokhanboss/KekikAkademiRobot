# https://github.com/Quiec/AsenaUserBot

from pyrogram import Client, Filters
import asyncio

@Client.on_message(Filters.command(['basaramadik'], ['!','.','/']) & Filters.me)
async def basaramadik(client, message):
    await asyncio.sleep(0.3)
    ilk_mesaj = await message.edit("‌‌‎__asyncio.sleep(0.3)__")

    await ilk_mesaj.edit("Başaramadık Abi")

    animasyon = [
        "oLuM gE BurAyA QırMızi ŞortLi",
        "uLaN sEn bEnim EliMdeN tUttun İBiNe",
        "Benİ bUrdan YuQarı ÇekMedİn ULAN",
        "bEn boĞuLim ÇeQmeDin bEnİ",
        "sEnle MahMüd",
        "BAŞARAMADIK ABİ",
        "nEyi BAşaraMadıN AmınaGoyim",
        "...",
        "GüLme OğlıM ŞerEfSız",
        "**QırMızi ŞortLi SuNar**"
        ]
    
    for anime in animasyon:
        await asyncio.sleep(0.7)
        await ilk_mesaj.edit(anime)
    
    await asyncio.sleep(3)

    yarak = '...............▄▄ ▄▄\n......▄▌▒▒▀▒▒▐▄\n.... ▐▒▒▒▒▒▒▒▒▒▌\n... ▐▒▒▒▒▒▒▒▒▒▒▒▌\n....▐▒▒▒▒▒▒▒▒▒▒▒▌\n....▐▀▄▄▄▄▄▄▄▄▄▀▌\n....▐░░░░░░░░░░░▌\n....▐░░░░░░░░░░░▌\n....▐░░░░░░░░░░░▌\n....▐░░░░░░░░░░░▌\n....▐░░░░░░░░░░░▌\n....▐░░░░░░░░░░░▌\n....▐░░░░░░░░░░░▌\n....▐░░░░░░░░░░░▌\n....▐░░░░░░░░░░░▌\n....▐░░░░░░░░░░░▌\n....▐░░░░░░░░░░░▌\n...▄█▓░░░░░░░░░▓█▄\n..▄▀░░░░░░░░░░░░░ ▀▄\n.▐░░░░░░░▀▄▒▄▀░░░░░░▌\n▐░░░░░░░▒▒▐▒▒░░░░░░░▌\n▐▒░░░░░▒▒▒▐▒▒▒░░░░░▒▌\n.▀▄▒▒▒▒▒▄▀▒▀▄▒▒▒▒▒▄▀\n.. ▀▀▀▀▀ ▀▀▀▀▀'

    await ilk_mesaj.edit(yarak)
    
    await ilk_mesaj.delete()