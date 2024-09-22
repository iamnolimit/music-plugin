import random

from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from config import LOG_GROUP_ID
from main import app
from main.utils.database import add_served_chat, get_assistant

photo = [
    "https://telegra.ph/file/1949480f01355b4e87d26.jpg",
    "https://telegra.ph/file/3ef2cc0ad2bc548bafb30.jpg",
    "https://telegra.ph/file/a7d663cd2de689b811729.jpg",
    "https://telegra.ph/file/6f19dc23847f5b005e922.jpg",
    "https://telegra.ph/file/2973150dd62fd27a3a6ba.jpg",
]



@app.on_message(filters.new_chat_members, group=-10)
async def join_watcher(_, message):
    try:
        userbot = await get_assistant(message.chat.id)
        chat = message.chat
        for members in message.new_chat_members:
            if members.id == app.id:
                count = await app.get_chat_members_count(chat.id)
                username = (
                    message.chat.username if message.chat.username else "𝐏ʀɪᴠᴀᴛᴇ 𝐆ʀᴏᴜᴘ"
                )
                msg = (
                    f"ʙᴏᴛ ᴀᴅᴅᴇᴅ ɪɴ ɴᴇᴡ ɢʀᴏᴜᴘ\n\n"
                    f"ᴄʜᴀᴛ ɴᴀᴍᴇ : {message.chat.title}\n"
                    f"ᴄʜᴀᴛ ɪᴅ : `{message.chat.id}`\n"
                    f"ᴄʜᴀᴛ ᴜꜱɴ : @{username}\n"
                    f"ᴍᴇᴍʙᴇʀꜱ : {count}\n"
                    f"ᴀᴅᴅᴇᴅ ʙʏ : {message.from_user.mention}"
                )
                await app.send_photo(
                    LOG_GROUP_ID,
                    photo=random.choice(photo),
                    caption=msg,
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton(
                                    f"ᴀᴅᴅᴇᴅ ʙʏ",
                                    url=f"tg://openmessage?user_id={message.from_user.id}",
                                )
                            ]
                        ]
                    ),
                )
                await add_served_chat(message.chat.id)
                await userbot.join_chat(f"{username}")
                

    except Exception as e:
        print(f"Error: {e}")





























