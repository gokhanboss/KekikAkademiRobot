# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from pyrogram import Client, Filters
import asyncio
import requests
import os

@Client.on_message(Filters.command(['pastever'], ['!','.','/']))
async def pastever(client, message):
    await message.reply_chat_action("typing")
    cevaplanan_mesaj = message.reply_to_message
    girilen_yazi = message.text
    await asyncio.sleep(0.3)

    if cevaplanan_mesaj is None:
        ilk_mesaj = await message.reply("__asyncio.sleep(0.3)__")
        if len(girilen_yazi.split()) == 1:
            await ilk_mesaj.edit("Paste yapabilmek için `kod` ve `uzantı` vermelisiniz..")
            return
        elif len(girilen_yazi.split()) == 2:
            await ilk_mesaj.edit("Paste yapabilmek için `uzantı` da vermelisiniz..\n\n`.pastever py`")
            return
    else:
        ilk_mesaj = await message.reply("__asyncio.sleep(0.3)__", reply_to_message_id = cevaplanan_mesaj.message_id)
        if len(girilen_yazi.split()) == 1:
            await ilk_mesaj.edit("Paste yapabilmek için `uzantı` da vermelisiniz..\n\n`.pastever py`")
            return

    uzanti = message.text.split()[1]
    kod = " ".join(girilen_yazi.split()[2:])
    await ilk_mesaj.delete()
    
    sonuc = requests.post(f"https://hastebin.com/documents", data = kod.encode("utf-8")).json()

    await message.reply(f'https://hastebin.com/{sonuc["key"]}.{uzanti}',
                  disable_web_page_preview  = True,
                  reply_to_message_id       = cevaplanan_mesaj.message_id
                  )

@Client.on_message(Filters.command(['pasteal'], ['!','.','/']))
async def pasteal(client, message):
    await asyncio.sleep(0.3)
    ilk_mesaj = await message.reply("__asyncio.sleep(0.3)__")
    
    cevaplanan_mesaj = message.reply_to_message

    if cevaplanan_mesaj is None:
        await ilk_mesaj.edit("__script'e çevrilecek hastebin linki yanıtlamanız gerekli..__")
        return
    elif not cevaplanan_mesaj.text.startswith("https://hastebin.com"):
        await ilk_mesaj.edit("__sadece hastebin linki yanıtlaman gerekli..__")
        return
    
    kod = message.reply_to_message.text.split('/')[-1]
    uzanti = kod.split('.')[1]
    raw = 'https://hastebin.com/raw/' + kod.split('.')[0]
    
    try:
        data = requests.get(raw).content
    except Exception as hata:
        await ilk_mesaj.edit(f'**Hata**\n__Muhtemelen yanıtladığın mesajda sadece link yok..__\n\n\t`{hata}`')

    await ilk_mesaj.delete()

    with open(f'{kod}', "wb+") as dosya: dosya.write(data)
    
    await message.reply_document(
            document                    = f"{kod}",
            caption                     = '__KekikAkademi Robot tarafından dönüştürülmüştür__',
            disable_notification        = True,
            reply_to_message_id         = cevaplanan_mesaj.message_id
        )
    os.remove(f"{kod}")