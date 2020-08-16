# https://github.com/Skuzzy_xD/TelePyroBot

from pyrogram import Client, Filters
import pyfiglet
import asyncio

@Client.on_message(Filters.command(['figlet'], ['!','.','/']))
async def figlet(client, message):
    # < Başlangıç
    await message.reply_chat_action("typing")
    await asyncio.sleep(0.3)
    uyku = await message.reply("__asyncio.sleep(0.3)__")

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

    girilen_yazi = message.text                               # komut ile birlikle mesajı tut

    if len(girilen_yazi.split()) == 1:                        # eğer sadece komut varsa
        await ilk_mesaj.edit("__bişiler söyle__")             # uyarı ver
        return                                                # geri dön

    neDedi = " ".join(girilen_yazi.split()[1:])               # sözü komuttan ayır

    sonuc = pyfiglet.figlet_format(neDedi)
    await asyncio.sleep(0.3)
    await ilk_mesaj.edit(f"‌‌‎`{sonuc}`")
