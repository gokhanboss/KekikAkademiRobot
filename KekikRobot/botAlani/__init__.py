# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from pyrogram import Client, Filters
import json

bilgiler = json.load(open("bilgiler.json"))

kekikRobot        = Client(
    api_id          = bilgiler['api_id'],                   # my.telegram.org/apps
    api_hash        = bilgiler['api_hash'],                 # my.telegram.org/apps
    session_name    = "@kekikRobot",                        # Fark Etmez
    bot_token       = bilgiler['bot_token'],                # @BotFather
    plugins         = dict(root="botAlani/Eklentiler")
)

# başlıyoruz

from time import time, sleep
from os import listdir

@kekikRobot.on_message(Filters.command(['start'], ['!','.','/']))
async def ilk(client, message):
    # Hoş Geldin Mesajı
    await message.reply_chat_action("typing")                           # yazıyor aksiyonu
    await message.reply("Hoş Geldin!\n/yardim alabilirsin.")            # cevapla

    # LOG Alanı
    sohbet = await kekikRobot.get_chat(message.chat.id)
    log = f"[{message.from_user.first_name}](tg://user?id={message.from_user.id})"
    if message.chat.type != 'private':
        log += f"\n\n\t\t`{sohbet.title}`__'den__ `{message.text}` __yolladı..__"
    else:
        log += f"\n\n\t\t`{message.text}` __yolladı..__"
    log +=  f"\n\n**Sohbet Türü :** __{message.chat.type}__"
    await client.send_message(bilgiler['log_id'], log)                        # admin_id'ye log gönder
    #-------------------------------------------------------------------------#

@kekikRobot.on_message(Filters.command(['yardim'], ['!','.','/']))
async def yardim_mesaji(client, message):
    await message.reply_chat_action("typing")

    cevaplanan_mesaj = message.reply_to_message

    if cevaplanan_mesaj is None:
        ilk_mesaj = await message.reply("__Bekleyin..__")
    else:
        ilk_mesaj = await message.reply("__Bekleyin..__", reply_to_message_id = cevaplanan_mesaj.message_id)
    
    basla = time()
    await ilk_mesaj.edit("__Aranıyor...__")

    mesaj = f"""Merhaba, [{message.from_user.first_name}](tg://user?id={message.from_user.id})!\n
    Ben @KekikAkademi'de yaratıldım.\n
    Kaynak kodlarım [Burada](http://bc.vc/FvAcrkp)
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

    # LOG Alanı
    sohbet = await kekikRobot.get_chat(message.chat.id)
    log = f"[{message.from_user.first_name}](tg://user?id={message.from_user.id})"
    if message.chat.type != 'private':
        log += f"\n\n\t\t`{sohbet.title}`__'den__ `{message.text}` __yolladı..__"
    else:
        log += f"\n\n\t\t`{message.text}` __yolladı..__"
    log +=  f"\n\n**Sohbet Türü :** __{message.chat.type}__"
    await client.send_message(bilgiler['log_id'], log)                        # admin_id'ye log gönder
    #-------------------------------------------------------------------------#

@kekikRobot.on_message(Filters.command(['eklenti'], ['!','.','/']))
async def eklenti_gonder(client, message):
    await message.reply_chat_action("typing")

    cevaplanan_mesaj = message.reply_to_message
    if cevaplanan_mesaj is None:
        ilk_mesaj = await message.reply("__Bekleyin..__")
    else:
        ilk_mesaj = await message.reply("__Bekleyin..__", reply_to_message_id=cevaplanan_mesaj.message_id)
    
    girilen_yazi = message.text                                 # komut ile birlikle mesajı tut

    if len(girilen_yazi.split()) == 1:                          # eğer sadece komut varsa
        await ilk_mesaj.edit("`DosyaAdı` **Girmelisin!**")      # uyarı ver
        return                                                  # geri dön

    dosya = " ".join(girilen_yazi.split()[1:2])                 # dosyayı komuttan ayır (birinci kelime)

    if f"{dosya}.py" in listdir("botAlani/Eklentiler"):
        await ilk_mesaj.delete()

        if cevaplanan_mesaj is not None:
            await message.reply_document(
                document                = f"./botAlani/Eklentiler/{dosya}.py",
                caption                 = f"__kekikRobot__ `{dosya}` __eklentisi..__",
                disable_notification    = True,
                reply_to_message_id     = cevaplanan_mesaj.message_id
                )
        else:
            await message.reply_document(
                document                = f"./botAlani/Eklentiler/{dosya}.py",
                caption                 = f"__kekikRobot__ `{dosya}` __eklentisi..__",
                disable_notification    = True,
                )

    else:
        await ilk_mesaj.edit('**Dosya Bulunamadı!**')
    
    # LOG Alanı
    sohbet = await kekikRobot.get_chat(message.chat.id)
    log = f"[{message.from_user.first_name}](tg://user?id={message.from_user.id})"
    if message.chat.type != 'private':
        log += f"\n\n\t\t`{sohbet.title}`__'den__ `{message.text}` __yolladı..__"
    else:
        log += f"\n\n\t\t`{message.text}` __yolladı..__"
    log +=  f"\n\n**Sohbet Türü :** __{message.chat.type}__"
    await client.send_message(bilgiler['log_id'], log)                        # admin_id'ye log gönder
    #-------------------------------------------------------------------------#