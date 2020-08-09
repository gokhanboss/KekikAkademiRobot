# https://github.com/Skuzzy_xD/TelePyroBot

from pyrogram import Message, Client, Filters
import asyncio

async def admin_check(message: Message) -> bool:
    client = message._client
    chat_id = message.chat.id
    user_id = message.from_user.id

    check_status = await client.get_chat_member(
        chat_id=chat_id,
        user_id=user_id
    )
    admin_strings = [
        "creator",
        "administrator"
    ]
    if check_status.status not in admin_strings:
        return False
    else:
        return True

@Client.on_message(Filters.command("dell", ['!','.','/']) & Filters.me)
async def purge(client, message):
    if message.chat.type in ("supergroup", "channel"):
        await message.edit("`Puuufff`")
        is_admin = await admin_check(message)
        if not is_admin:
            await message.edit("Admin değilmişim :)")
            await asyncio.sleep(2)
            await message.delete()
            return
    if message.chat.type in ["private", "bot", "group"]:
        await message.edit("`Bu komutu burda kullanamazsın..`")
        await asyncio.sleep(2)
        await message.delete()
        return

    message_ids = []
    count_del_etion_s = 0

    if message.reply_to_message:
        for a_s_message_id in range(message.reply_to_message.message_id, message.message_id):
            message_ids.append(a_s_message_id)
            if len(message_ids) == 100:
                await client.delete_messages(
                    chat_id=message.chat.id,
                    message_ids=message_ids,
                    revoke=True)
                count_del_etion_s += len(message_ids)
                message_ids = []
        if len(message_ids) > 0:
            await client.delete_messages(
                chat_id=message.chat.id,
                message_ids=message_ids,
                revoke=True)
            count_del_etion_s += len(message_ids)

    await message.edit(f"`<u>{count_del_etion_s}</u> Adet Mesaj Silindi`")
    await asyncio.sleep(3)
    await message.delete()

@Client.on_message(Filters.command("del", ['!','.','/']) & Filters.me, group=3)
async def del_msg(client, message):
    if message.reply_to_message:
        if message.chat.type in ("supergroup", "channel"):
            is_admin = await admin_check(message)
            if not is_admin:
                await message.reply("`Admin değilmişim :)`")
                await asyncio.sleep(3)
                await message.delete()
                return

        await client.delete_messages(
            chat_id=message.chat.id,
            message_ids=message.reply_to_message.message_id)

    else:
        await message.edit("`Silmek istediğin mesajı yanıtla..`")

    await asyncio.sleep(1)
    await message.delete()