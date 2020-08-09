# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from pyrogram import Client, Filters
import asyncio
import requests
import os

@Client.on_message(Filters.command(['pastever'], ['!','.','/']))
async def pastever(client, message):
    await asyncio.sleep(0.3)
    ilk_mesaj = await message.reply("__asyncio.sleep(0.3)__")

    if message.reply_to_message:
        kod = message.reply_to_message.text
        yanitlanacakMesaj = message.reply_to_message.message_id
    else:
        if len(message.text.split()) == 1:
            return
        kod = " ".join(message.text.split()[2:])
        yanitlanacakMesaj = message.message_id
    
    uzanti = message.text.split()[1]
    await ilk_mesaj.delete()

    sonuc = requests.post(f"https://hastebin.com/documents", data = kod.encode("utf-8")).json()

    await message.reply(f'https://hastebin.com/{sonuc["key"]}.{uzanti}',
                  disable_web_page_preview  = True,
                  reply_to_message_id       = yanitlanacakMesaj
                  )

@Client.on_message(Filters.command(['pasteal'], ['!','.','/']))
async def pasteal(client, message):
    await asyncio.sleep(0.3)
    ilk_mesaj = await message.reply("__asyncio.sleep(0.3)__")

    kod = message.reply_to_message.text.split('/')[-1]
    uzanti = kod.split('.')[1]
    raw = 'https://hastebin.com/raw/' + kod.split('.')[0]

    await ilk_mesaj.delete()

    with open(f'{kod}', "w+") as dosya: dosya.write(raw)
    
    await message.reply_document(
            document                    = f"{kod}",
            caption                     = '__ilk_mesajSonu UserBot tarafından dönüştürülmüştür__',
            disable_notification        = True,
            reply_to_message_id         = message.reply_to_message.message_id
        )
    os.remove(f"{kod}")