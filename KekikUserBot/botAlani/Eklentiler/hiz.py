# https://github.com/Skuzzy_xD/TelePyroBot

from pyrogram import Client, Filters
from speedtest import Speedtest

@Client.on_message(Filters.command("hiz", ['!','.','/']) & Filters.me)
async def hiztesti(client, message):
    ilk_mesaj = await message.edit("`Hız testi yapılıyor . . .`")
    test = Speedtest()
    test.get_best_server()
    test.download()
    test.upload()
    test.results.share()
    result = test.results.dict()
    await ilk_mesaj.edit("**Başlama Zamanı:** "
                       f"`{result['timestamp']}`\n\n"
                       "**Download:** "
                       f"`{speed_convert(result['download'])}`\n"
                       "**Upload:** "
                       f"`{speed_convert(result['upload'])}`\n"
                       "**Ping:** "
                       f"`{result['ping']} ms`\n"
                       "**ISP:** "
                       f"`{result['client']['isp']}`",
                       parse_mode="markdown")


def speed_convert(size):
    power = 2 ** 10
    zero = 0
    units = {0: '', 1: 'Kb/s', 2: 'Mb/s', 3: 'Gb/s', 4: 'Tb/s'}
    while size > power:
        size /= power
        zero += 1
    return f"{round(size, 2)} {units[zero]}"