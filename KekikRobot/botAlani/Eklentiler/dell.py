# https://github.com/Skuzzy_xD/TelePyroBot

from pyrogram import Message, Client, Filters
import asyncio
import json
from botAlani import bilgiler

@Client.on_message(Filters.command("dell", ['!','.','/']))
async def purge(client, message):
    ilk_mesaj = await message.reply("`Puuufff`")

    cevaplanan_mesaj = message.reply_to_message

    if cevaplanan_mesaj is None:
        await ilk_mesaj.edit("__içinden geçmek istediğiniz yerden mesaj yanıtlayın__")
        return
    
    if message.chat.type in ("supergroup", "channel"):
        if message.from_user.id != bilgiler['kurucu']:
            await ilk_mesaj.edit(f"Admin değilmişim :)\n\n`{message.from_user.id}` __!=__ `{bilgiler['kurucu']}`")
            await asyncio.sleep(2)
            await ilk_mesaj.delete()
            return
    
    elif message.chat.type in ["private", "bot", "group"]:
        await ilk_mesaj.edit("`Bu komutu burda kullanamazsın..`")
        await asyncio.sleep(2)
        await ilk_mesaj.delete()
        return
    
    silinecek_mesaj_idleri = []
    silinen_mesaj_sayisi = 0

    if message.reply_to_message:
        for say_mesaj_id in range(message.reply_to_message.message_id, message.message_id):
            silinecek_mesaj_idleri.append(say_mesaj_id)
        
        if len(silinecek_mesaj_idleri) > 0:
            await client.delete_messages(
                chat_id     = message.chat.id,
                message_ids = silinecek_mesaj_idleri,
                revoke      = True
                )
            silinen_mesaj_sayisi += len(silinecek_mesaj_idleri)

    await ilk_mesaj.edit(f"`<u>{silinen_mesaj_sayisi}</u> Adet Mesaj Silindi`")
    await asyncio.sleep(3)