# https://github.com/SkuzzyxD/TelePyroBot/blob/master/telepyrobot/plugins/plugin_manager.py

from pyrogram import Client, filters
import asyncio, os

@Client.on_message(filters.command(['eklentilist'], ['!','.','/']) & filters.me)
async def eklenti_list(client, message):
    # < Başlangıç
    await message.reply_chat_action("typing")
    await asyncio.sleep(0.3)
    uyku = await message.edit("__asyncio.sleep(0.3)__")

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

    mesaj = "__Eklentilerim;__\n"

    for dosya in os.listdir("./userBot/botAlani/Eklentiler/"):
        if not dosya.endswith(".py"):
            continue
        mesaj += f"📂 `{dosya.replace('.py','')}`\n"
    
    try:
        await ilk_mesaj.edit(mesaj)
    except Exception as hata:
        await ilk_mesaj.edit(f"**Uuppss:**\n\n`{hata}`")

@Client.on_message(filters.command(['eklentiver'], ['!','.','/']) & filters.me)
async def eklenti_ver(client, message):
    # < Başlangıç
    await message.reply_chat_action("typing")
    await asyncio.sleep(0.3)
    uyku = await message.edit("__asyncio.sleep(0.3)__")

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
    
    girilen_yazi = message.text                                 # komut ile birlikle mesajı tut

    if len(girilen_yazi.split()) == 1:                          # eğer sadece komut varsa
        await ilk_mesaj.edit("`DosyaAdı` **Girmelisin!**")      # uyarı ver
        return                                                  # geri dön

    dosya = " ".join(girilen_yazi.split()[1:2])                 # dosyayı komuttan ayır (birinci kelime)

    if f"{dosya}.py" in os.listdir("userBot/botAlani/Eklentiler"):
        await ilk_mesaj.delete()

        await message.reply_document(
            document                = f"./userBot/botAlani/Eklentiler/{dosya}.py",
            caption                 = f"__kekikUserBot__ `{dosya}` __eklentisi..__",
            disable_notification    = True,
            reply_to_message_id     = yanitlanacak_mesaj
            )

    else:
        await ilk_mesaj.edit('**Dosya Bulunamadı!**')

@Client.on_message(filters.command(['eklential'], ['!','.','/']) & filters.me)
async def eklenti_al(client, message):
    # < Başlangıç
    await message.reply_chat_action("typing")
    await asyncio.sleep(0.3)
    uyku = await message.edit("__asyncio.sleep(0.3)__")

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
    
    if len(message.command) == 1 and cevaplanan_mesaj.document:
        if cevaplanan_mesaj.document.file_name.split(".")[-1] != "py":
            await ilk_mesaj.edit("`Yalnızca python dosyası yükleyebilirsiniz..`")
            return
        eklenti_dizini = f"./userBot/botAlani/Eklentiler/{cevaplanan_mesaj.document.file_name}"
        await ilk_mesaj.edit("`Eklenti Yükleniyor...`")
        
        if os.path.exists(eklenti_dizini):
            await ilk_mesaj.edit(f"`{cevaplanan_mesaj.document.file_name}` __eklentisi zaten mevcut!__")
            return
        
        try:
            eklenti_indir = await client.download_media(message=cevaplanan_mesaj, file_name=eklenti_dizini)
            if eklenti_indir:
                await message.edit(f"**Eklenti Yüklendi:** `{cevaplanan_mesaj.document.file_name}`")
                return
        
        except Exception as hata:
            await ilk_mesaj.edit(f"**Uuppss:**\n\n`{hata}`")
    
    await ilk_mesaj.edit('__python betiği yanıtlamanız gerekmekte__')
    return


@Client.on_message(filters.command(['eklentisil'], ['!','.','/']) & filters.me)
async def eklenti_sil(client, message):
    # < Başlangıç
    await message.reply_chat_action("typing")
    await asyncio.sleep(0.3)
    uyku = await message.edit("__asyncio.sleep(0.3)__")

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
    
    if len(message.command) == 2:
        eklenti_dizini = f"./userBot/botAlani/Eklentiler/{message.command[1]}.py"
        
        if os.path.exists(eklenti_dizini):
            os.remove(eklenti_dizini)
            await ilk_mesaj.edit(f"**Eklenti Silindi:** `{message.command[1]}`")
            return
        
        await ilk_mesaj.edit("`Böyle bir eklenti yok`")
        return
    
    await ilk_mesaj.edit("`Geçerli bir eklenti adı girin!`")
    return