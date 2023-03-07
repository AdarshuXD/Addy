#Addy @AdarshuXd
import requests
import random
import os
import re
import asyncio
import time
from datetime import datetime

from pyrogram import Client, filters
from pyrogram.types import *

from pymongo import MongoClient
from motor.motor_asyncio import AsyncIOMotorClient as MongoCli


API_ID = int(os.environ.get("API_ID", None))
API_HASH = os.environ.get("API_HASH", None) 
BOT_TOKEN = os.environ.get("BOT_TOKEN", None) 
MONGO_URL = os.environ.get("MONGO_URL", None)
BOT_USERNAME = os.environ.get("BOT_USERNAME") 
UPDATE_CHNL = os.environ.get("UPDATE_CHNL")
OWNER_ID = int(os.environ.get("OWNER_ID"))
OWNER_USERNAME = os.environ.get("OWNER_USERNAME")
SUPPORT_GRP = os.environ.get("SUPPORT_GRP")
BOT_NAME = os.environ.get("BOT_NAME")
START_IMG1 = os.environ.get("START_IMG1")
START_IMG2 = os.environ.get("START_IMG2")
START_IMG3 = os.environ.get("START_IMG3")
START_IMG4 = os.environ.get("START_IMG4")
START_IMG5 = os.environ.get("START_IMG5")
START_IMG6 = os.environ.get("START_IMG6")
START_IMG7 = os.environ.get("START_IMG7")
START_IMG8 = os.environ.get("START_IMG8")
START_IMG9 = os.environ.get("START_IMG9")
START_IMG10 = os.environ.get("START_IMG10")
STKR = os.environ.get("STKR", "CAACAgQAAxkBAALRimNZXTpB8mhQbnAAAWAvCV4Ya1uHFQACnxEAAqbxcR57wYUDyflSISoE")
STKR1 = os.environ.get("STKR1", "CAACAgQAAxkBAALRi2NZXUgjZCT775L5Nr0XrLbQ6XIpAAK_EQACpvFxHq2xh5JRVJNrKgQ")
STKR2 = os.environ.get("STKR2", "CAACAgQAAxkBAALRjGNZXUs6YPggISBdtg4nXaU0vjNzAALqCwACbCIRU61ZQKi3F88DKgQ")
STKR3 = os.environ.get("STKR3", "CAACAgQAAxkBAALRjWNZXUvETcfHR2Yi9ftTQLLP2uD8AAIVDAAC1SMQU-QrCHEcbz8rKgQ")
STKR4 = os.environ.get("STKR4", "CAACAgQAAxkBAALRjmNZXWw-WbZ_iAg-4UGixa7WSz3RAAK9CQACelwRUzpqVCTmeOrfKgQ")
STKR5 = os.environ.get("STKR5", "CAACAgQAAxkBAALRj2NZXXJw6Pw7TJgYQStoq4u2oYpmAAKgEQACpvFxHk7lQeNrq3NMKgQ")
STKR6 = os.environ.get("STKR6", "CAACAgQAAxkBAALRkGNZXYmAXYRR4lmCxHGPgG012Vm0AAJiFwACpvFxHuCsJc_EpuEVKgQ")
STKR7 = os.environ.get("STKR7", "CAACAgQAAxkBAALRkWNZXYyCvkfI4d1lK0AEMkG0GdUmAAJmFwACpvFxHnvJHTM8_o9XKgQ")
STKR8 = os.environ.get("STKR8", "CAACAgQAAxkBAALRkmNZXZg1zuakmgkPf2lfXPXi4bZaAALACgACQUGpUjAAAYL3e09XCyoE")

bot = Client(
    "Addy" ,
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
)

mongo = MongoCli(MONGO_URL)
db = mongo.Anonymous
chatsdb = db.chatsdb
usersdb = db.users

async def is_admins(chat_id: int):
    return [
        member.user.id
        async for member in bot.iter_chat_members(
            chat_id, filter="administrators"
        )
    ]


PHOTO = [
    START_IMG1,
    START_IMG2,
    START_IMG3,
    START_IMG4,
    START_IMG5,
    START_IMG6,
    START_IMG7,
    START_IMG8,
    START_IMG9,
    START_IMG10,
]

EMOJIOS = [ 
      "💣",
      "💥",
      "🪄",
      "🧨",
      "⚡",
      "🤡",
      "👻",
      "🎃",
      "🎩",
      "🕊",
]
      
STICKER = [
      STKR,
      STKR1,
      STKR2,
      STKR3,
      STKR4,
      STKR5,
      STKR6,
      STKR7,
      STKR8,
]
START = f"""
**• Hey, I am [{BOT_NAME}]({START_IMG1})**
**➻ An AI Based ChatBot**
**──────────────**
**➻ Usage /chatbot [ᴏɴ/ᴏғғ]**
<b>||• Hit Help Button For Help.||</b>
"""
DEV_OP = [
    [
        InlineKeyboardButton(text="🥀 Owner 🥀", url=f"t.me/{OWNER_USERNAME}"),
        InlineKeyboardButton(text="✨Support✨", url=f"https://t.me/{SUPPORT_GRP}"),
    ],
    [
        InlineKeyboardButton(
            text="🧸 Add Me Baby🧸",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
    [
        InlineKeyboardButton(text="🚀 Help & Cmds 🚀", callback_data="HELP"),
    ],
    [
        InlineKeyboardButton(text="❄️Source❄️", callback_data="SOURCE"),
        InlineKeyboardButton(text="☁️About☁️", callback_data="ABOUT"),
    ],
]
PNG_BTN = [
    [
         InlineKeyboardButton(
             text="🧸 Add Me Baby 🧸",
             url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
         ),
     ],
     [
         InlineKeyboardButton(
             text="✨ Support ✨", 
             url=f"https://t.me/{SUPPORT_GRP}",
         ),
     ],
]
HELP_READ = f"""
<u>**Commands For {BOT_NAME}**</u>
<u>**Are Given Below!**</u>
**All The Commands Can Be Used With:/**
**──────────────**
<b>||©️ @{OWNER_USERNAME}||</b>
"""
BACK = [
     [
           InlineKeyboardButton(text="✨ Back ✨", callback_data="BACK"),
     ],
]
HELP_BTN = [
     [
          InlineKeyboardButton(text="🐳 Chatbot 🐳", callback_data="CHATBOT_CMD"),
          InlineKeyboardButton(text="🎄 Tools 🎄", callback_data="TOOLS_DATA"),
     ],
     [
          InlineKeyboardButton(text="✨ Back ✨", callback_data="BACK"),
          InlineKeyboardButton(text="❄️ Close ❄️", callback_data="CLOSE"),
     ],
]

CLOSE_BTN = [
      [
           InlineKeyboardButton(text="❄️ Close ❄️", callback_data="CLOSE"),
      ],
]

CHATBOT_ON = [
        [
            InlineKeyboardButton(text="Enable", callback_data=f"addchat"),
            InlineKeyboardButton(text="Disable", callback_data=f"rmchat"),
        ],
]

PNG_BTN = [
    [
         InlineKeyboardButton(
             text="🧸 Add Me Baby 🧸",
             url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
         ),
     ],
     [
         InlineKeyboardButton(text="✨ Close ✨", 
                              callback_data="CLOSE",
         ),
     ],
]

TOOLS_DATA_READ = f"""
<u>**Tools For {BOT_NAME} ᴀʀᴇ:**</u>
**──────────────**
**➻ Use `/ping` For Checking The Ping Of{BOT_NAME}**
**──────────────**
<b>||©️ @{OWNER_USERNAME}||</b>
"""

async def is_served_user(user_id: int) -> bool:
    user = await usersdb.find_one({"user_id": user_id})
    if not user:
        return False
    return True

async def get_served_users() -> list:
    users_list = []
    async for user in usersdb.find({"user_id": {"$gt": 0}}):
        users_list.append(user)
    return users_list

async def add_served_user(user_id: int):
    is_served = await is_served_user(user_id)
    if is_served:
        return
    return await usersdb.insert_one({"user_id": user_id})

async def get_served_chats() -> list:
    chats = chatsdb.find({"chat_id": {"$lt": 0}})
    if not chats:
        return []
    chats_list = []
    for chat in await chats.to_list(length=1000000000):
        chats_list.append(chat)
    return chats_list

async def is_served_chat(chat_id: int) -> bool:
    chat = await chatsdb.find_one({"chat_id": chat_id})
    if not chat:
        return False
    return True


async def add_served_chat(chat_id: int):
    is_served = await is_served_chat(chat_id)
    if is_served:
        return
    return await chatsdb.insert_one({"chat_id": chat_id})

CHATBOT_READ = f"""
<u>**Commands For {BOT_NAME}**</u>
**➻ Use `/chatbot` To Enable/Disable The ChatBot.**
**๏Note ➻ The Above Command For ChatBot Work In Group Only!!**
**───────────────**
<b>||©️ @{OWNER_USERNAME}||</b>
"""
CHATBOT_BACK = [
        [     
              InlineKeyboardButton(text="✨ Back ✨", callback_data="CHATBOT_BACK"),
              InlineKeyboardButton(text="❄️ Close ❄️", callback_data="CLOSE"),
        ],
]
HELP_START = [
     [
            InlineKeyboardButton(text="🚀 Help 🚀", callback_data="HELP"),
            InlineKeyboardButton(text="🐳 Close 🐳", callback_data="CLOSE"),
     ],
]

HELP_BUTN = [
     [
           InlineKeyboardButton(text="🚀 Help 🚀", url=f"https://t.me/{BOT_USERNAME}?start=help"),
           InlineKeyboardButton(text="🐳 Close 🐳", callback_data="CLOSE"),
     ],
]

ABOUT_BTN = [
      [
           InlineKeyboardButton(text="🎄 Support 🎄", url=f"https://t.me/{SUPPORT_GRP}"),  
           InlineKeyboardButton(text="🚀 Help 🚀", callback_data="HELP"),
      ],
      [    
           InlineKeyboardButton(text="🍾 Owner 🍾", url=f"https://t.me/{OWNER_USERNAME}"), 
           InlineKeyboardButton(text="❄️ Source ❄️", callback_data="SOURCE"),
      ],
      [ 
           InlineKeyboardButton(text="🐳 Update 🐳", url=f"https://t.me/{UPDATE_CHNL}"),  
           InlineKeyboardButton(text="✨ Back ✨", callback_data="BACK"),
      ],
]
SOURCE_READ = f"**Hey, The Source Code Of[{BOT_NAME}](https://t.me/{BOT_USERNAME}) Is Given Below.**\n**Please Fork The Repo & Give The Star ✯**\n**──────────────────**\n**Here Is The Source Code [sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ Source Code](Love_You_Ad.t.me)**\n**──────────────────**\n**If You Face Any Problem Then Conty At[Support Chat](https://t.me/{SUPPORT_GRP}).\n<b>||©️ @{OWNER_USERNAME}||</b>"

ABOUT_READ = f"""
**➻ [{BOT_NAME}](https://t.me/{BOT_USERNAME}) Is An AI Based Chat-Bot.**
**➻ [{BOT_NAME}](https://t.me/{BOT_USERNAME}) Replies Automatically To a User.**
**➻ Helps You In Activating Your Groups.**
**➻ Written In [Python](https://www.python.org) With [Mongo-DM](https://www.mongodb.com) As A Database**
**──────────────**
**➻ Click On The Buttons Given Below For Getting Basic Help And Info About [{BOT_NAME}](https://t.me/{BOT_USERNAME})**
"""
@bot.on_message(filters.command(["start", "aistart", f"start@{BOT_USERNAME}"]))
async def restart(client, m: Message):
    if m.chat.type == "private":
        accha = await m.reply_text(
            text = random.choice(EMOJIOS),
        )
        await asyncio.sleep(1.3)
        await accha.edit("Hehehe...Ding Dong 🥀 Starting.......__")
        await asyncio.sleep(0.2)
        await accha.edit("Hehehe...Ding Dong 🥀 Starting.......__")
        await asyncio.sleep(0.2)
        await accha.edit("Hehehe...Ding Dong 🥀 Starting.......__")
        await asyncio.sleep(0.2)
        await accha.delete()
        umm = await m.reply_sticker(sticker=random.choice(STICKER))
        await asyncio.sleep(2)
        await umm.delete()
        await m.reply_photo(
            photo = random.choice(PHOTO),
            caption=f"""**๏ Hey, I'm [{BOT_NAME}](t.me/{BOT_USERNAME})**\n**➻ An AI Based ChatBot.**\n**──────────────**\n**➻ Usage /chatbot [ᴏɴ/ᴏғғ]**\n<b>||๏ Hit Help Button For Help||</b>""",
            reply_markup=InlineKeyboardMarkup(DEV_OP),
        )
        await add_served_user(m.from_user.id)
    else:
        await m.reply_photo(
            photo=random.choice(PHOTO),
            caption=START,
            reply_markup=InlineKeyboardMarkup(HELP_START),
        )
        await add_served_chat(m.chat.id)

@bot.on_callback_query()
async def cb_handler(Client, query: CallbackQuery):
    vickdb = MongoClient(MONGO_URL)
    vick = vickdb["VickDb"]["Vick"]
    if query.data == "HELP":
        await query.message.edit_text(
                      text = HELP_READ,
                      reply_markup=InlineKeyboardMarkup(HELP_BTN),
                      disable_web_page_preview=True,
     )
    elif query.data == "CLOSE":
            await query.message.delete()
    elif query.data == "BACK":
            await query.message.edit(
                  text = START,
                  reply_markup=InlineKeyboardMarkup(DEV_OP),
     )
    elif query.data == "SOURCE":
            await query.message.edit(
                   text = SOURCE_READ,
                   reply_markup = InlineKeyboardMarkup(BACK),
                   disable_web_page_preview = True,

     )
    elif query.data == "ABOUT":
            await query.message.edit(
                    text = ABOUT_READ,
                    reply_markup = InlineKeyboardMarkup(ABOUT_BTN),
                    disable_web_page_preview=True,
     )
    elif query.data == "ADMINS":
            await query.message.edit(
                    text = ADMIN_READ,
                    reply_markup = InlineKeyboardMarkup(MUSIC_BACK_BTN), 
     )
    elif query.data== "TOOLS_DATA":
            await query.message.edit(
                    text= TOOLS_DATA_READ,
                    reply_markup = InlineKeyboardMarkup(CHATBOT_BACK),
     )
    elif query.data == "BACK_HELP":
            await query.message.edit(
                    text = HELP_READ,
                    reply_markup = InlineKeyboardMarkup(HELP_BTN),
     )
    elif query.data == "CHATBOT_CMD":
            await query.message.edit(
                    text = CHATBOT_READ,
                    reply_markup = InlineKeyboardMarkup(CHATBOT_BACK), 
     )
    elif query.data == "CHATBOT_BACK":
            await query.message.edit(
                    text = HELP_READ,
                    reply_markup = InlineKeyboardMarkup(HELP_BTN), 
     )
    elif query.data == "addchat":
        if query.from_user.id not in (await is_admins(query.message.chat.id)):
            return query.answer(
                "You don't have permissions to do this baby.",
                show_alert=True,
            )
        else:
            is_vick = vick.find_one({"chat_id": query.message.chat.id})
            if not is_vick:           
                await query.edit_message_text(f"**Chat-Bot Already Enabled**")
            if is_vick:
                vick.delete_one({"chat_id": query.message.chat.id})
                await query.edit_message_text(f"**Chat-Bot Enabled By** {query.from_user.mention}.")
    elif query.data == "rmchat":
        if query.from_user.id not in (await is_admins(query.message.chat.id)):
            return query.answer(
                "**You Don't Have Perms To Do This Babe!**",
                show_alert=True,
            )
        else:
            is_vick = vick.find_one({"chat_id": query.message.chat.id})
            if not is_vick:
                vick.insert_one({"chat_id": query.message.chat.id})
                await query.edit_message_text(f"**Chat-Bot Disabled By** {query.from_user.mention}.")
            if is_vick:
                await query.edit_message_text("**Chat-Bot Already Disable.**")
                            
@bot.on_message(filters.command("repo"))
async def repo(client, message):
    await message.reply_text(
       text=SOURCE_READ,
       reply_markup=InlineKeyboardMarkup(CLOSE_BTN),
       disable_web_page_preview=True,
    )

@bot.on_message(filters.command(["help", f"help@{BOT_USERNAME}"], prefixes=["+", ".", "/", "-", "?", "$"]))
async def restart(client, m: Message):
    if m.chat.type == "private":
        hmm = await m.reply_photo(
            photo=random.choice(PHOTO),
            caption=HELP_READ,
            reply_markup=InlineKeyboardMarkup(HELP_BTN),
        )
        await add_served_user(m.from_user.id)
    else:
        await m.reply_photo(
            photo=random.choice(PHOTO),
            caption="**Hey, Babe Pm Me For Help Commands!**",
            reply_markup=InlineKeyboardMarkup(HELP_BUTN),
        )
        await add_served_chat(m.chat.id)


@bot.on_message(filters.command("stats") & filters.user(OWNER_ID))
async def get_st(_, msg: Message):
    users = len(await get_served_users())
    chats = len(await get_served_chats())
    await msg.reply_photo(
        photo="https://telegra.ph/file/76ad7bbcb112404cf34a3.jpg",
        caption=f"Total Stats Of {BOT_NAME}\n\n➻ **Chats :** {chats}\n➻ **User :** {users}",
    )

@bot.on_message(filters.command("ping", prefixes=["+", "/", "-", "?", "$", "&"]))
async def ping(client, message: Message):
    if message.chat.type == "private":
        await add_served_user(message.from_user.id)
    else:
        await add_served_chat(message.chat.id)
    await message.delete()
    start = datetime.now()
    wtfbhemchomd = await message.reply_sticker(sticker= random.choice(STICKER))
    ms = (datetime.now()-start).microseconds / 1000
    await message.reply_photo(
        photo=random.choice(PHOTO),
        caption=f"Hey baby!!\n**[{BOT_NAME}](t.me/{BOT_USERNAME})** Is Alive 🥀 And Working Fine With A ping Of\n➥ `{ms}` ms\n\n<b||Made With 💕 By [Developer](https://t.me/{OWNER_USERNAME})||</b>",
        reply_markup=InlineKeyboardMarkup(PNG_BTN),
    )

                  
@bot.on_message(
    filters.command(["chatbot", f"chatbot@{BOT_USERNAME}"])
    & ~filters.private)
async def chatonoff(client: Client, message: Message):
    if not message.from_user:
        return
    else:
        user = message.from_user.id
        chat_id = message.chat.id
        if user not in (await is_admins(chat_id)):
            return await message.reply_text(
                "**You Aren't Admin Babh.**"
            )
        else:
            await message.reply_text(
            text="» <u>**Choose an Option To Enable/Disable ChatBot.**</u>",
            reply_markup=InlineKeyboardMarkup(CHATBOT_ON),
        )


@bot.on_message(
 (
        filters.text
        | filters.sticker
    )
    & ~filters.private
    & ~filters.bot,
)
async def vickai(client: Client, message: Message):

   chatdb = MongoClient(MONGO_URL)
   chatai = chatdb["Word"]["WordDb"]   

   if not message.reply_to_message:
       vickdb = MongoClient(MONGO_URL)
       vick = vickdb["VickDb"]["Vick"] 
       is_vick = vick.find_one({"chat_id": message.chat.id})
       if not is_vick:
           await bot.send_chat_action(message.chat.id, "typing")
           K = []  
           is_chat = chatai.find({"word": message.text})  
           k = chatai.find_one({"word": message.text})      
           if k:               
               for x in is_chat:
                   K.append(x['text'])          
               hey = random.choice(K)
               is_text = chatai.find_one({"text": hey})
               Yo = is_text['check']
               if Yo == "sticker":
                   await message.reply_sticker(f"{hey}")
               if not Yo == "sticker":
                   await message.reply_text(f"{hey}")
   
   if message.reply_to_message:  
       vickdb = MongoClient(MONGO_URL)
       vick = vickdb["VickDb"]["Vick"] 
       is_vick = vick.find_one({"chat_id": message.chat.id})    
       getme = await bot.get_me()
       bot_id = getme.id                             
       if message.reply_to_message.from_user.id == bot_id: 
           if not is_vick:                   
               await bot.send_chat_action(message.chat.id, "typing")
               K = []  
               is_chat = chatai.find({"word": message.text})
               k = chatai.find_one({"word": message.text})      
               if k:       
                   for x in is_chat:
                       K.append(x['text'])
                   hey = random.choice(K)
                   is_text = chatai.find_one({"text": hey})
                   Yo = is_text['check']
                   if Yo == "sticker":
                       await message.reply_sticker(f"{hey}")
                   if not Yo == "sticker":
                       await message.reply_text(f"{hey}")
       if not message.reply_to_message.from_user.id == bot_id:          
           if message.sticker:
               is_chat = chatai.find_one({"word": message.reply_to_message.text, "id": message.sticker.file_unique_id})
               if not is_chat:
                   chatai.insert_one({"word": message.reply_to_message.text, "text": message.sticker.file_id, "check": "sticker", "id": message.sticker.file_unique_id})
           if message.text:                 
               is_chat = chatai.find_one({"word": message.reply_to_message.text, "text": message.text})                 
               if not is_chat:
                   chatai.insert_one({"word": message.reply_to_message.text, "text": message.text, "check": "none"})    
               

@bot.on_message(
 (
        filters.sticker
        | filters.text
    )
    & ~filters.private
    & ~filters.bot,
)
async def vickstickerai(client: Client, message: Message):

   chatdb = MongoClient(MONGO_URL)
   chatai = chatdb["Word"]["WordDb"]   

   if not message.reply_to_message:
       vickdb = MongoClient(MONGO_URL)
       vick = vickdb["VickDb"]["Vick"] 
       is_vick = vick.find_one({"chat_id": message.chat.id})
       if not is_vick:
           await bot.send_chat_action(message.chat.id, "typing")
           K = []  
           is_chat = chatai.find({"word": message.sticker.file_unique_id})      
           k = chatai.find_one({"word": message.text})      
           if k:           
               for x in is_chat:
                   K.append(x['text'])
               hey = random.choice(K)
               is_text = chatai.find_one({"text": hey})
               Yo = is_text['check']
               if Yo == "text":
                   await message.reply_text(f"{hey}")
               if not Yo == "text":
                   await message.reply_sticker(f"{hey}")
   
   if message.reply_to_message:
       vickdb = MongoClient(MONGO_URL)
       vick = vickdb["VickDb"]["Vick"] 
       is_vick = vick.find_one({"chat_id": message.chat.id})
       getme = await bot.get_me()
       bot_id = getme.id
       if message.reply_to_message.from_user.id == bot_id: 
           if not is_vick:                    
               await bot.send_chat_action(message.chat.id, "typing")
               K = []  
               is_chat = chatai.find({"word": message.text})
               k = chatai.find_one({"word": message.text})      
               if k:           
                   for x in is_chat:
                       K.append(x['text'])
                   hey = random.choice(K)
                   is_text = chatai.find_one({"text": hey})
                   Yo = is_text['check']
                   if Yo == "text":
                       await message.reply_text(f"{hey}")
                   if not Yo == "text":
                       await message.reply_sticker(f"{hey}")
       if not message.reply_to_message.from_user.id == bot_id:          
           if message.text:
               is_chat = chatai.find_one({"word": message.reply_to_message.sticker.file_unique_id, "text": message.text})
               if not is_chat:
                   toggle.insert_one({"word": message.reply_to_message.sticker.file_unique_id, "text": message.text, "check": "text"})
           if message.sticker:                 
               is_chat = chatai.find_one({"word": message.reply_to_message.sticker.file_unique_id, "text": message.sticker.file_id})                 
               if not is_chat:
                   chatai.insert_one({"word": message.reply_to_message.sticker.file_unique_id, "text": message.sticker.file_id, "check": "none"})    
               


@bot.on_message(
    (
        filters.text
        | filters.sticker
    )
    & filters.private
    & ~filters.bot,
)
async def vickprivate(client: Client, message: Message):

   chatdb = MongoClient(MONGO_URL)
   chatai = chatdb["Word"]["WordDb"]
   if not message.reply_to_message: 
       await bot.send_chat_action(message.chat.id, "typing")
       K = []  
       is_chat = chatai.find({"word": message.text})                 
       for x in is_chat:
           K.append(x['text'])
       hey = random.choice(K)
       is_text = chatai.find_one({"text": hey})
       Yo = is_text['check']
       if Yo == "sticker":
           await message.reply_sticker(f"{hey}")
       if not Yo == "sticker":
           await message.reply_text(f"{hey}")
   if message.reply_to_message:            
       getme = await bot.get_me()
       bot_id = getme.id       
       if message.reply_to_message.from_user.id == bot_id:                    
           await bot.send_chat_action(message.chat.id, "typing")
           K = []  
           is_chat = chatai.find({"word": message.text})                 
           for x in is_chat:
               K.append(x['text'])
           hey = random.choice(K)
           is_text = chatai.find_one({"text": hey})
           Yo = is_text['check']
           if Yo == "sticker":
               await message.reply_sticker(f"{hey}")
           if not Yo == "sticker":
               await message.reply_text(f"{hey}")
       

@bot.on_message(
 (
        filters.sticker
        | filters.text
    )
    & filters.private
    & ~filters.bot,
)
async def vickprivatesticker(client: Client, message: Message):

   chatdb = MongoClient(MONGO_URL)
   chatai = chatdb["Word"]["WordDb"] 
   if not message.reply_to_message:
       await bot.send_chat_action(message.chat.id, "typing")
       K = []  
       is_chat = chatai.find({"word": message.sticker.file_unique_id})                 
       for x in is_chat:
           K.append(x['text'])
       hey = random.choice(K)
       is_text = chatai.find_one({"text": hey})
       Yo = is_text['check']
       if Yo == "text":
           await message.reply_text(f"{hey}")
       if not Yo == "text":
           await message.reply_sticker(f"{hey}")
   if message.reply_to_message:            
       getme = await bot.get_me()
       bot_id = getme.id       
       if message.reply_to_message.from_user.id == bot_id:                    
           await bot.send_chat_action(message.chat.id, "typing")
           K = []  
           is_chat = chatai.find({"word": message.sticker.file_unique_id})                 
           for x in is_chat:
               K.append(x['text'])
           hey = random.choice(K)
           is_text = chatai.find_one({"text": hey})
           Yo = is_text['check']
           if Yo == "text":
               await message.reply_text(f"{hey}")
           if not Yo == "text":
               await message.reply_sticker(f"{hey}")

print(f"{BOT_NAME} Is Alive! Now Fuck Off And Go To @AddyChannel Bitch!!")      
bot.run()
