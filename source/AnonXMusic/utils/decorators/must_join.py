from AnonXMusic import app
from pyrogram.types import Message, InlineKeyboardMarkup as ikm, InlineKeyboardButton as ikb
from pyrogram.errors import UserNotParticipant
import asyncio 
import requests
import json
from AnonXMusic.utils.database import get_must, get_must_ch
from config import BOT_TOKEN

def must_join_ch(zohary):
  async def ch_user(c,msg):
    if (await get_must(app.username)) and (await get_must_ch(app.username) == "مفعل"):
      i = await get_must(app.username)
      s = requests.get(f"https://api.telegram.org/bot{BOT_TOKEN}/getChatMember?chat_id=@{i}&user_id={msg.from_user.id}")
      data = s.json()
      if data["ok"] and data["result"]["status"] in ["member","creator","administrator"]:
        return await zohary(c,msg)
      else:
        return await msg.reply(f"- يجب الاشتراك بالقناه اولا لاستخدام البوت \n - @{i} .",disable_web_page_preview=True,reply_markup=ikm([[ikb("اضغط للاشتراك بالقناه.",url=f"https://t.me/{i}")],]))
    else: return await zohary(c,msg)
  return ch_user
