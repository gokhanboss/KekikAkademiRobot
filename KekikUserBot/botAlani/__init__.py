# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from pyrogram import Client, Filters
import json

bilgiler = json.load(open("bilgiler.json"))

kekikUserBot        = Client(
    api_id          = bilgiler['api_id'],                   # my.telegram.org/apps
    api_hash        = bilgiler['api_hash'],                 # my.telegram.org/apps
    session_name    = "@kekikUserBot",                      # Fark Etmez
    plugins         = dict(root="botAlani/Eklentiler")
)

from time import time, sleep
from os import listdir

@kekikUserBot.on_message(Filters.command(['yardim'], ['!','.','/']) & Filters.me)
async def yardim_mesaji(client, message):
    ilk_mesaj = await message.edit("__Bekleyin..__")
    basla = time()
    await ilk_mesaj.edit("__Aranıyor...__")

    mesaj = f"""Merhaba, [{message.from_user.first_name}](tg://user?id={message.from_user.id})!\n
    Ben @KekikAkademi'de yaratıldım.\n
    Kaynak kodlarım [Burada](https://github.com/keyiflerolsun/KekikAkademiRobot)
    Kullanabileceğim komutlar ise eklentilerimde gizli..\n\n"""

    mesaj += "__Eklentilerim;__\n"

    for dosya in listdir("./botAlani/Eklentiler/"):
        if not dosya.endswith(".py"):
            continue
        mesaj += f"📂 `{dosya.replace('.py','')}`\n"

    bitir = time()
    sure = bitir - basla
    mesaj += f"\n**Tepki Süresi :** `{str(sure)[:4]} sn`"

    try:
        await ilk_mesaj.edit(mesaj, disable_web_page_preview = True, parse_mode = "Markdown")
    except Exception as hata_mesaji:
        await ilk_mesaj.edit(hata_mesaji)

@kekikUserBot.on_message(Filters.command(['eklenti'], ['!','.','/']) & Filters.me)
async def eklenti_gonder(client, message):
    ilk_mesaj = await message.edit("__Bekleyin..__")
    
    if message.reply_to_message:                                # Eğer mesaj yanıtlanan bir mesaj ise
        yanitlanacakMesaj = message.reply_to_message.message_id
    else:
        yanitlanacakMesaj = message.message_id
    
    girilen_yazi = message.text                                 # komut ile birlikle mesajı tut

    if len(girilen_yazi.split()) == 1:                          # eğer sadece komut varsa
        await ilk_mesaj.edit("`DosyaAdı` **Girmelisin!**")      # uyarı ver
        return                                                  # geri dön

    dosya = " ".join(girilen_yazi.split()[1:2])                 # dosyayı komuttan ayır (birinci kelime)

    if f"{dosya}.py" in listdir("botAlani/Eklentiler"):
        await ilk_mesaj.delete()
        await message.reply_document(
            document                = f"./botAlani/Eklentiler/{dosya}.py",
            caption                 = f"__kekikUserBot__ `{dosya}` __eklentisi..__",
            disable_notification    = True,
            reply_to_message_id     = yanitlanacakMesaj
            )
    else:
        await ilk_mesaj.edit('**Dosya Bulunamadı!**')