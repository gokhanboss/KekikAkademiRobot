# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from pyrogram import Client, Filters
from os import remove
import requests
from bs4 import BeautifulSoup

def neNedir(ne):
    url = f"https://www.google.com/search?&q={ne} nedir? 'wiki'" + "&lr=lang_tr&hl=tr"
    kimlik = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}

    istek = requests.get(url, kimlik)
    corba = BeautifulSoup(istek.text, "lxml")

    nedir = corba.find('div', class_='BNeawe').text
    
    return f"**{ne.capitalize()}**\n\n__{nedir}__"

# print(nedir("aristokrasi") + '\n')
# print(nedir("kürek") + '\n')
# print(nedir("restoran") + '\n')
# print(nedir("laparoskopi") + '\n')

@Client.on_message(Filters.command(['nedir'],['!','.','/']))
async def nedir(client, message):
    cevaplanan_mesaj = message.reply_to_message
    
    if cevaplanan_mesaj is None:
        ilk_mesaj = await message.reply("__Bekleyin..__")
    else:
        ilk_mesaj = await message.reply("__Bekleyin..__", reply_to_message_id=cevaplanan_mesaj.message_id)

    girilen_yazi = message.text
    if len(girilen_yazi.split()) == 1:
        await ilk_mesaj.edit("Arama yapabilmek için `bişeyler` girmelisiniz")
        return
    
    bakalim = " ".join(girilen_yazi.split()[1:])

    try:
        mesaj = neNedir(bakalim)
    except Exception as hata:
        mesaj = f"__Bir hata ile karşılaştım ;__\n\n`{hata}`"

    try:
        await ilk_mesaj.edit(mesaj, disable_web_page_preview=True, parse_mode="Markdown")
    except Exception as hata_mesaji:
        await ilk_mesaj.edit(hata_mesaji)
