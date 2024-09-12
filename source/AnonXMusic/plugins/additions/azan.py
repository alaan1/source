from datetime import datetime
from backports.zoneinfo import ZoneInfo
from adhanpy.calculation import CalculationMethod
from adhanpy.PrayerTimes import PrayerTimes
from pyrogram import Client, filters
from AnonXMusic import app
from AnonXMusic.core.call import Anony
from AnonXMusic.utils.database import get_assistant
from pyrogram.errors import UserNotParticipant, InviteRequestSent
from pyrogram.enums import ChatMemberStatus
import requests, os, asyncio

zone = ZoneInfo("Africa/Cairo")

def azan_time():
  pray = PrayerTimes((30.033, 31.233), datetime.now(), CalculationMethod.EGYPTIAN, time_zone = zone)
  if pray.fajr.strftime("%H:%M") == datetime.now(zone).strftime("%H:%M"):
    return "الفجر"
  if pray.dhuhr.strftime("%H:%M") == datetime.now(zone).strftime("%H:%M"):
    return "الظهر"
  if pray.asr.strftime("%H:%M") == datetime.now(zone).strftime("%H:%M"):
    return "العصر"
  if pray.maghrib.strftime("%H:%M") == datetime.now(zone).strftime("%H:%M"):
    return "المغرب"
  if pray.isha.strftime("%H:%M") == datetime.now(zone).strftime("%H:%M"):
    return "العشاء"

chats = []

async def azan_run():
  while not await asyncio.sleep(2):
    if azan_time():
      pray = azan_time()
      for i in chats:
        try:
            await Anony.stop_stream(i)
            await app.send_message(i, f"حان الان صلاة {pray} .")
            try:
              await Anony.join_call(i,i, "AnonXMusic/assets/319070.mp3")
            except Exception as e:
              print(e)
        except:
            pass
      await asyncio.sleep(250)

@app.on_message(filters.command(["تفعيل الاذان$", "تعطيل الاذان$"],""))
async def en_dis_azan(c, msg):
  if msg.chat.id in chats:
    if msg.text[:2] == "تف":
      return await msg.reply("- الاذان مفعل بالفعل")
    else:
      chats.remove(msg.chat.id)
      return await msg.reply("- تم تعطيل الاذان.")
  else:
    if msg.text[:2] == "تف":
      chats.append(msg.chat.id)
      user = await get_assistant(msg.chat.id)
      try:
        member = await c.get_chat_member(msg.chat.id, user.id)
        if member.status in [ChatMemberStatus.BANNED, ChatMemberStatus.RESTRICTED]:
          return await msg.reply(f" تم تفعيل تنبيه الاذان ولكن يجب فك حظر او تقييد الحساب المساعد لكي يقوم بتشغيل الاذان بالمحادثة الصوتيه ف وقتها . \n - يوزر الحساب المساعد : @{user.username} .")
      except UserNotParticipant:
        try:
          link = msg.chat.username if msg.chat.username else (await app.export_chat_invite_link(msg.chat.id)).replace("https://t.me/+", "https://t.me/joinchat/")
          await user.join_chat(link)
        except InviteRequestSent:
          try: 
            await app.approve_chat_join_request(msg.chat.id, user.id)
          except Exception as e: 
            await msg.reply(e)
      return await msg.reply("- تم تفعيل الاذان.")
    else:
      return await msg.reply("- الاذان معطل بالفعل")
