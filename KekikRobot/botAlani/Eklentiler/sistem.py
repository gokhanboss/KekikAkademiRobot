# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from pyrogram import Client, Filters
import asyncio
import requests, os, platform

@Client.on_message(Filters.command(['sistem'], ['!','.','/']))
async def sistem(client, message):
    await asyncio.sleep(0.3)
    ilk_mesaj = await message.reply("__asyncio.sleep(0.3)__")
    
    try:
        mesaj = f"""__Kullanıcı :__ `{os.getlogin()}@{platform.node()}`
    __IP :__ `{requests.get('http://ip.42.pl/raw').text}`
    __OS :__ `{platform.system()} | {platform.release()}`
    __İşlemci :__ `{platform.processor()}`"""
        await ilk_mesaj.edit(mesaj)
    
    except Exception as hata:
        await ilk_mesaj.edit(f"__başaramadık abi__\n\n\t`{hata}`")
