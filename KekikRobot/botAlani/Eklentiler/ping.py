# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from pyrogram import Client, Filters
import asyncio
import datetime

@Client.on_message(Filters.command(['ping'], ['!','.','/']))
async def ping(client, message):
    basla = datetime.datetime.now()
    ilk_mesaj = await message.reply("Bekleyin..")

    mesaj = "__Pong!__"

    bitir = datetime.datetime.now()
    sure = (bitir - basla).microseconds/10000
    mesaj += f"\n\n**Tepki Süresi :** `{sure} ms`"

    await ilk_mesaj.edit(mesaj)
    
    await asyncio.sleep(3)
    await ilk_mesaj.edit("__şimdi mutlu musun?__")
    await asyncio.sleep(1)
    await ilk_mesaj.edit(mesaj)