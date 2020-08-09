# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from pyrogram import Client, Filters
from os import remove
import requests
from bs4 import BeautifulSoup

def havaDurumu(sehir):
    url = f"https://www.google.com/search?&q={sehir} hava durumu"
    kimlik = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}

    istek = requests.get(url, kimlik)
    corba = BeautifulSoup(istek.text, "lxml")

    gun_durum = corba.findAll('div', class_='BNeawe')
    gun, durum = gun_durum[3].text.strip().split('\n')
    derece = corba.find('div', class_='BNeawe').text

    return f"**{sehir.capitalize()}**\n\t__{gun}__\n\t\t`{durum} {derece}`"

# print(havaDurumu("mumbai"))
# print(havaDurumu("bahreyn"))
# print(havaDurumu("brüksel"))
# print(havaDurumu("çanakkale"))
# print(havaDurumu("new york"))

@Client.on_message(Filters.command(['hava'],['!','.','/']) & Filters.me)
async def hava(client, message):
    cevaplanan_mesaj = message.reply_to_message
    
    if cevaplanan_mesaj is None:
        ilk_mesaj = await message.edit("__Bekleyin..__")
    else:
        ilk_mesaj = await message.edit("__Bekleyin..__", reply_to_message_id=cevaplanan_mesaj.message_id)

    girilen_yazi = message.text
    if len(girilen_yazi.split()) == 1:
        await ilk_mesaj.edit("Arama yapabilmek için `şehir` girmelisiniz")
        return
    
    sehir = " ".join(girilen_yazi.split()[1:2])

    try:
        mesaj = havaDurumu(sehir)
    except Exception as hata:
        mesaj = f"__Bir hata ile karşılaştım ;__\n\n`{hata}`"

    try:
        await ilk_mesaj.edit(mesaj, disable_web_page_preview=True, parse_mode="Markdown")
    except Exception as hata_mesaji:
        await ilk_mesaj.edit(hata_mesaji)
