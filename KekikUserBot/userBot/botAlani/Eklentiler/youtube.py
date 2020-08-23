# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from pyrogram import Client, Filters
import asyncio
from pytube import YouTube
import os

@Client.on_message(Filters.command(['youtube'], ['!','.','/']))
async def youtube(client, message):
    # < Başlangıç
    uyku = await message.edit("__asyncio.sleep(0.3)__")
    await asyncio.sleep(0.3)
    
    cevaplanan_mesaj    = message.reply_to_message
    if cevaplanan_mesaj is None:
        yanitlanacak_mesaj  = message.message_id
    else:
        yanitlanacak_mesaj = cevaplanan_mesaj.message_id
    
    await uyku.delete()
    ilk_mesaj = await message.reply("__Bekleyin..__",
        reply_to_message_id         = yanitlanacak_mesaj,
        disable_web_page_preview    = True,
        parse_mode                  = "Markdown"
    )
    #------------------------------------------------------------- Başlangıç >

    girilen_yazi = message.text
    if len(girilen_yazi.split()) == 1:
        await ilk_mesaj.edit("Arama yapabilmek için `bişeyler` girmelisiniz")
        return
    
    verilen_link = " ".join(girilen_yazi.split()[1:])

    if len(verilen_link.split()) > 1:
        mesaj = "**Yalnızca Link Verin**"
        return
    elif not verilen_link.startswith('http://youtube.com') or not verilen_link.startswith('https://youtube.com'):
        mesaj = "**Link** `http://youtube.com` **ile başlamalıdır..**"
        return
    
    video = YouTube(verilen_link).streams.get_highest_resolution().download()
    await client.send_video(message.chat.id, video)
    os.remove(video)

    try:
        await ilk_mesaj.edit(mesaj)
    except Exception as hata:
        await ilk_mesaj.edit(f"**Uuppss:**\n\n`{hata}`")