# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from pyrogram import Client, Filters
from os import remove
import requests
from bs4 import BeautifulSoup

def nobetciEczane(il, ilce):
    url = f"https://www.eczaneler.gen.tr/nobetci-{il}-{ilce}"
    kimlik = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}

    istek = requests.get(url, kimlik)
    corba = BeautifulSoup(istek.text, "lxml")
    
    eczane_adi = []
    eczane_adresi = []
    eczane_telefonu = []

    for tablo in corba.find('div', id='nav-bugun'):
        for ad in tablo.findAll('span', class_='isim'):
            eczane_adi.append(ad.text)

        for adres in tablo.findAll('span', class_='text-capitalize'):
            eczane_adresi.append(adres.text)

        for telefon in tablo.findAll('div', class_='col-lg-3 py-2'):
            eczane_telefonu.append(telefon.text)
        
    liste = []
    for adet in range(0, len(eczane_adi)):
        sozluk = {}
        sozluk['eczane_adi'] = eczane_adi[adet]
        sozluk['eczane_adresi'] = eczane_adresi[adet]
        sozluk['eczane_telefonu'] = eczane_telefonu[adet]
        liste.append(sozluk)

    return liste

# print(nobetci("canakkale", "merkez"))

# import json
# print(json.dumps(nobetci("canakkale", "merkez"), indent=2, sort_keys=False, ensure_ascii=False))

@Client.on_message(Filters.command(['nobetci'],['!','.','/']) & Filters.me)
async def nobetci(client, message):
    cevaplanan_mesaj = message.reply_to_message
    
    if cevaplanan_mesaj is None:
        ilk_mesaj = await message.edit("__Bekleyin..__")
    else:
        ilk_mesaj = await message.edit("__Bekleyin..__", reply_to_message_id=cevaplanan_mesaj.message_id)

    girilen_yazi = message.text
    if len(girilen_yazi.split()) == 1:
        await ilk_mesaj.edit("Arama yapabilmek için `il` ve `ilçe` girmelisiniz")
        return
    elif len(girilen_yazi.split()) == 2:
        await ilk_mesaj.edit("Arama yapabilmek için `ilçe` de girmelisiniz")
        return

    tr2eng = str.maketrans(" .,-*/+-ıİüÜöÖçÇşŞğĞ", "________iIuUoOcCsSgG")
    il = " ".join(girilen_yazi.split()[1:2]).translate(tr2eng)          # il'i komuttan ayrıştır (birinci kelime)
    ilce = " ".join(girilen_yazi.split()[2:3]).translate(tr2eng)        # ilçe'yi komuttan ayrıştır (ikinci kelime)
    mesaj = f"Aranan Nöbetçi Eczane : `{ilce}` / `{il}`\n"

    try:
        for i in nobetciEczane(il, ilce):
            mesaj += f"**\n{i['eczane_adi']}**\n__{i['eczane_adresi']}__\n`{i['eczane_telefonu']}`\n\n"
    except Exception as hata:
        mesaj = f"__Bir hata ile karşılaştım ;__\n\n`{hata}`"

    try:
        await ilk_mesaj.edit(mesaj, disable_web_page_preview=True, parse_mode="Markdown")
    except Exception as hata_mesaji:
        await ilk_mesaj.edit(hata_mesaji)
