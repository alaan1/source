import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from AnonXMusic import app, Telegram
from AnonXMusic.misc import SUDOERS
from pyrogram.enums import ChatType
from config import OWNER_ID, SUPPORT_CHANNEL, SUPPORT_CHAT

async def huhh(client: Client, message: Message): 
    await message.reply_photo(
        photo=f"https://t.me/Y_z_Q",
        caption=f"• 𝗧𝗵𝗲 𝗕𝗲𝘀𝘁 𝗦𝗼𝘂𝗿𝗰𝗲 𝗢𝗻 𝗧𝗲𝗹𝗲𝗴𝗮𝗺 🎸 .",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "- 𝖲𝗈𝖴𝖱𝖢𝖾 .", url=SUPPORT_CHANNEL),
                    InlineKeyboardButton(
                        "- Help .", url=SUPPORT_CHAT),
                    
                ],[
                    InlineKeyboardButton(
                        "- DeVeLoPeRS .", callback_data=f"developers {message.from_user.id}" if message.chat.type != ChatType.CHANNEL else "developers ch"),
                ],

            ]

        ),

    )



@app.on_message(
    filters.command(["سورس$","السورس$","صورص$"],"")
)
async def source(c, msg):
  if msg.chat.type == ChatType.CHANNEL:
      await huhh(c, msg)
  else:
    if not msg.sender_chat:
       await huhh(c, msg)

async def zohary(client: Client, message: Message, dev_id):
  usr = await app.get_users(dev_id)
  user = await client.get_chat(dev_id)
  Bio = user.bio
  name = usr.first_name
  ms = "‹ Dev Sourse ›\n\n" if message.text != "المطور" else "‹ Dev Bot ›\n\n" + f"D e v | - {usr.mention} .\n"
  if usr.username:
      ms += f"U s e r d e v | - @{usr.username} .\n"
  if Bio:
      ms += f"B i o | - {Bio} ."
  async for photo in app.get_chat_photos(dev_id,limit=1):
    await message.reply_photo(photo.file_id, caption=ms,
        reply_markup=InlineKeyboardMarkup(
              [              
                [          
                  InlineKeyboardButton (name, user_id=dev_id)
                ],             
              ]                 
           )                     
        )


@app.on_message(filters.command(["يوصف","زوهري","المطور حسين","حسين","المبرمج حسين","المطور", "مطور البوت", "مطور السورس"],""),group=-8)
async def rd_zohary(c,msg):
  if msg.chat.type == ChatType.CHANNEL:
      if msg.text in ["حسين","حسين","المبرمج حسين", "مطور السورس"]:
        await zohary(c, msg, 6687004499)
      elif msg.text in ["المطور", "مطور البوت"]:
        try:
            await app.resolve_peer(OWNER_ID)
            OWNER = OWNER_ID
        except:
            OWNER = None
        await zohary(c,msg,OWNER) 
  else:
    if not msg.sender_chat:
      if msg.text in ["حسين","حسين","المبرمج حسين", "مطور السورس"]:
        await zohary(c, msg, 6687004499)
      elif msg.text in ["المطور", "مطور البوت"]:
        try:
            await app.resolve_peer(OWNER_ID)
            OWNER = OWNER_ID
        except:
            OWNER = None
        await zohary(c,msg,OWNER) 
       
