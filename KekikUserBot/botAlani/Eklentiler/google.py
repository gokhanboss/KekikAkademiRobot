# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from pyrogram import Client, Filters
from time import time
from google_search_client.search_client import GoogleSearchClient
import ast

@Client.on_message(Filters.command(['google'], ['!','.','/']) & Filters.me)
async def google(client, message):
    ilk_mesaj = await message.edit("Bekleyin..")
    
    girilen_yazi = message.text
    if len(girilen_yazi.split()) == 1:
        await ilk_mesaj.edit("Arama yapabilmek için kelime girmelisiniz..")
        return
    await ilk_mesaj.edit("Aranıyor...")
    
    basla = time()
    girdi = " ".join(girilen_yazi.split()[1:])
    mesaj = f"Aranan Kelime : `{girdi}`\n\n"
    
    istek = GoogleSearchClient()
    sonuclar = istek.search(girdi).to_json()
    
    if sonuclar:
        i = 1
        for sonuc in ast.literal_eval(sonuclar):
            mesaj += f"🔍 [{sonuc['title']}]({sonuc['url']})\n"
            i += 1
            if i == 5:
                break
        
        bitir = time()
        sure = bitir - basla
        mesaj += f"\nTepki Süresi : `{str(sure)[:4]} sn`"
        
        try:
            await ilk_mesaj.edit(mesaj, disable_web_page_preview=True, parse_mode="Markdown")
        except Exception as hata:
            await ilk_mesaj.edit(hata)
    else:
        await ilk_mesaj.edit("Hatalı bişeyler var, daha sonra tekrar deneyin..")