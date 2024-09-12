from pyrogram import Client, filters
from pyrogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, InlineKeyboardMarkup as ikm, InlineKeyboardButton as ikb 
from AnonXMusic import app
from config import OWNER_ID
from AnonXMusic.utils.database import get_served_chats, get_served_users, get_client, set_must, get_must, del_must, get_must_ch, set_must_ch, get_active_chats, remove_active_video_chat, remove_active_chat, get_served_channel
import os 
import shutil
import asyncio 

devs = filters.user([6687004499, 6938020788, OWNER_ID])

@app.on_message(filters.command(["start"]) & filters.private & devs, group = 2)
async def start_dev(c, msg):
    keyboard = ReplyKeyboardMarkup([[("• حذف الكيبورد •")], [("• مطور السورس •")], [("• قسم الاحصائيات •"), ("• قسم المساعد •")], [("• قسم الاشتراك الاجباري •"), ("• قسم الاذاعه •")], [("• اعادة التشغيل •")], [("• الغاء •")]], resize_keyboard=True)
    await msg.reply("<b>صلي على النبي وتبسم ♥️✨</b>")
    await msg.reply("<b>• اهلا بك حبيبي المطور◟</b>", reply_markup = keyboard)
    
@app.on_message(filters.command(["• حذف الكيبورد •"],"") & filters.private & devs, group = 2)
async def delete_keyboard(c,msg):
    await msg.reply("<b>• تم ازالة الكيبورد عزيزي المطور ◟</b>", reply_markup = ReplyKeyboardRemove())

@app.on_message(filters.command(["• قسم الاحصائيات •"],"") & filters.private & devs, group = 2)
async def stats_bot(c,msg):
    await msg.reply("<b>• اهلا بك عزيزي المطور بقسم الاحصائيات ◟</b>", reply_markup = ReplyKeyboardMarkup([[("• الجروبات •"), ("• المستخدمين •"), ("• القنوات •")], ["• رجوع للقائمة الرئيسية •"]], resize_keyboard=True))
    
@app.on_message(filters.command(["• قسم المساعد •"],"") & filters.private & devs, group = 2)
async def asisstant_bot(c,msg):
    await msg.reply("<b>• اهلا بك عزيزي المطور بقسم الاك المساعد ◟</b>", reply_markup = ReplyKeyboardMarkup([[("• تغيير الاسم الاول •"), ("• تغيير الاسم الثاني •")], [("• تغيير البايو •")], [("• اضف صورة •"), ("• مسح الصورة •")], [("• اذاعة •")], ["• رجوع للقائمة الرئيسية •"]], resize_keyboard=True))

@app.on_message(filters.command(["• قسم الاشتراك الاجباري •"],"") & filters.private & devs, group = 2)
async def force_sub_bot(c,msg):
    await msg.reply("<b>• اهلا بك عزيزي المطور بقسم الاشتراك الاجباري ◟</b>", reply_markup = ReplyKeyboardMarkup([[("• قناة الاشتراك •")], [("• اضف قناة/جروب •"), ("• حذف القناه/الجروب •")], [("• تفعيل الاشتراك •"), ("• تعطيل الاشتراك •")], ["• رجوع للقائمة الرئيسية •"]], resize_keyboard=True))

@app.on_message(filters.command(["• قسم الاذاعه •"],"") & filters.private & devs, group = 2)
async def broadcast_bot(c,msg):
    await msg.reply("<b>• اهلا بك عزيزي المطور بقسم الاذاعه ◟</b>", reply_markup = ReplyKeyboardMarkup([[("• للجروبات •"), ("• للمستخدمين •"), ("• للقنوات •")], [("• بالتوجيه للجروبات •"), ("• بالتوجيه للمستخدمين •"), ("• بالتوجيه للقنوات •")], [("• ترويج البوت •")], ["• رجوع للقائمة الرئيسية •"]], resize_keyboard=True))

@app.on_message(filters.command(["• رجوع للقائمة الرئيسية •"],"") & filters.private & devs, group = 2)
async def return_bot(c,msg):
    keyboard = ReplyKeyboardMarkup([[("• حذف الكيبورد •")], [("• مطور السورس •")], [("• قسم الاحصائيات •"), ("• قسم المساعد •")], [("• قسم الاشتراك الاجباري •"), ("• قسم الاذاعه •")], [("• اعادة التشغيل •")], [("• الغاء •")]], resize_keyboard=True)
    await msg.reply("<b>صلي على النبي وتبسم ♥️✨</b>")
    await msg.reply("<b>• اهلا بك حبيبي المطور◟</b>", reply_markup = keyboard)

@app.on_message(filters.command(["• الجروبات •", "• المستخدمين •", "• القنوات •"],"") & filters.private & devs, group = 2)
async def stat_bot(c,msg):
    if msg.text == "• المستخدمين •":
        served_users = len(await get_served_users())
        return await msg.reply(f"<b>• عدد مستخدمين البوت : {served_users} ◟</b>")
    elif msg.text == "• الجروبات •":
        served_chats = len(await get_served_chats())
        return await msg.reply(f"<b>• عدد جروبات البوت : {served_chats} ◟</b>")
    else:
        served_chats = len(await get_served_channel())
        return await msg.reply(f"<b>• عدد قنوات البوت : {served_chats} ◟</b>")

@app.on_message(filters.command(["• تغيير الاسم الاول •","• تغيير البايو •","• اضف صورة •","• تغيير الاسم الثاني •","• مسح الصورة •"],"") & filters.private & devs, group = 2)
async def acc_bot(c,msg):
    if msg.text == "• اضف صورة •":
        try:
            m = await c.ask(msg.chat.id, "<b>• قم بإرسال الصوره عزيزي المطور ◟</b>")
            if m.text == "• اضف صورة •":
                m = await c.ask(msg.chat.id, "<b>•عذرا قم بإرسال صورة عزيزي المطور ◟</b>")
            photo = await m.download()
            client = await get_client(1)
            await client.set_profile_photo(photo=photo)
            await msg.reply("<b>• تم تغيير الصورة بنجاح ◟</b>")
        except Exception as e:
            await msg.reply(f"- حدث خطا -> {e}")
    elif msg.text == "• تغيير البايو •":
        try:
            m = await c.ask(msg.chat.id, "• قم بإرسال البايو عزيزي المطور ◟")
            if m.text == "• تغيير البايو •":
                m = await c.ask(msg.chat.id, "<b>•عذرا قم بإرسال نص البايو عزيزي المطور ◟</b>")
            client = await get_client(1)
            await client.update_profile(bio=m.text)
            await msg.reply("• تم تغيير البايو بنجاح ◟")
        except Exception as e:
            await msg.reply(f"- حدث خطا -> {e}")
    elif msg.text == "• تغيير الاسم الاول •":
        try:
            m = await c.ask(msg.chat.id, "<b>• قم بإرسال الاسم عزيزي المطور ◟</b>")
            if m.text == "• تغيير الاسم الاول •":
                m = await c.ask(msg.chat.id, "<b>•عذرا قم بإرسال نص الاسم عزيزي المطور ◟</b>")
            client = await get_client(1)
            await client.update_profile(first_name=m.text)
            await msg.reply("<b>• تم تغيير الاسم الاول بنجاح ◟</b>")
        except Exception as e:
            await msg.reply(f"- حدث خطا -> {e}")
    elif msg.text == "• تغيير الاسم الثاني •":
        try:
            m = await c.ask(msg.chat.id, "<b>• قم بإرسال الاسم عزيزي المطور ◟</b>")
            if m.text == "• تغيير الاسم الثاني •":
                m = await c.ask(msg.chat.id, "<b>• عذرا قم بإرسال نص الاسم عزيزي المطور ◟</b>")
            client = await get_client(1)
            await client.update_profile(last_name=m.text)
            await msg.reply("<b>• تم تغيير الاسم التاني بنجاح ◟</b>")
        except Exception as e:
            await msg.reply(f"- حدث خطا -> {e}")
    else:
        client = await get_client(1)
        if (await client.get_me()).photo:
            try:
                async for photo in client.get_chat_photos("me", limit = 1):
                    await client.delete_profile_photos(photo.file_id)
                await msg.reply("<b>• تم حذف صورة من الحساب المساعد بنجاح◟</b>")
            except Exception as e:
                await msg.reply(f"- حدث خطا -> {e}")
        else:
            await msg.reply("• لا يوجد صور لحذفها عزيزي المطور ◟")

@app.on_message(filters.command(["• اذاعة •"],"") & filters.private & devs, group = 2)
async def broadcast_acc(c,msg):
    try:
        m = await c.ask(msg.chat.id, "• قم بإرسال الرسالة المراد نشرها عزيزي المطور ◟")
        if m.text == "• اذاعة •":
            m = await c.ask(msg.chat.id, "•عذرا قم بإرسال الرسالة المراد نشرها عزيزي المطور ◟")
        client = await get_client(1)
        x = 0
        async for ch in client.get_dialogs():
            try:
                if m.photo:
                    photo = await m.download()
                    await client.send_photo(ch.chat.id, photo=photo, caption=m.caption)
                elif m.video:
                    video = await m.download()
                    thumb = await app.download_media(m.video.thumbs[0].file_id)
                    await client.send_video(ch.chat.id, photo=video, caption=m.caption, duration=m.video.duration,thumb=thumb)
                else:
                    await client.send_message(ch.chat.id, text=m.text)
                x += 1
            except:
                pass
        await msg.reply(f"• تم ارسال الى {x} شات")
    except Exception as e:
        await msg.reply(f"- حدث خطا -> {e}")

@app.on_message(filters.command(["• اضف قناة/جروب •"],"") & filters.private & devs, group = 2)
async def add_must(c,msg):
    try:
        m = await c.ask(msg.chat.id, "•عذرا قم بإرسال يوزر القناها او الجروب وتاكد من رفع البوت بها عزيزي المطور ◟")
        try:
            chat = await c.get_chat(m.text)
        except:
            return await msg.reply("• تاكد عزيزي المطور من يوزر القناه او الجروب ◟")
        await set_must(c.me.username,chat.username)
        await msg.reply("• تم تعيين القناه بنجاح عزيزي المطور ◟")
    except Exception as e:
        await msg.reply(f"- حدث خطا -> {e}")

@app.on_message(filters.command(["• قناة الاشتراك •"],"") & filters.private & devs, group = 2)
async def get_ch_must(c,msg):
    db = await get_must(c.me.username)
    if db:
        return await msg.reply(f"• قناة الاشتراك : @{db} ◟")
    else:
        return await msg.reply("• لا يوجد عزيزي المطور قم باضافة قناة اولا ◟")

@app.on_message(filters.command(["• حذف القناه/الجروب •"],"") & filters.private & devs, group = 2)
async def rem_ch_must(c,msg):
    done = await del_must(c.me.username)
    if done:
        return await msg.reply("• تم حذف قناة الاشتراك الاجباري عزيزي المطور ◟")
    else:
        return await msg.reply("• لا يوجد عزيزي المطور لحذفه ◟")

@app.on_message(filters.command(["• تفعيل الاشتراك •"],"") & filters.private & devs, group = 2)
async def en_ch_must(c,msg):
    status = await get_must_ch(c.me.username)
    if status == "معطل" :
        await set_must_ch(c.me.username,"enable")
        await msg.reply("• تم تفعيل الاشتراك الاجباري عزيزي المطور ◟")
    else:
        await msg.reply("• الاشتراك الاجباري مفعل ◟")

@app.on_message(filters.command(["• تعطيل الاشتراك •"],"") & filters.private & devs, group = 2)
async def dis_ch_must(c,msg):
    status = await get_must_ch(c.me.username)
    if status == "مفعل" :
        await set_must_ch(c.me.username,"disable")
        await msg.reply("• تم تعطيل الاشتراك الاجباري عزيزي المطور ◟")
    else:
        await msg.reply("• الاشتراك الاجباري معطل ◟")

@app.on_message(filters.command(["• مطور السورس •"],"") & filters.private & devs, group = 2)
async def devs_source(c,msg):
    await msg.reply("• اهلا بك عزيزي المطور لرؤية معلومات المطورين قم بالضغط ع الاذرار بالاسفل ◟", reply_markup = ReplyKeyboardMarkup([[("• المطور الاول •"), ("• المطور الثاني •")], ["• رجوع للقائمة الرئيسية •"]], resize_keyboard=True))

@app.on_message(filters.command(["• المطور الاول •", "• المطور الثاني •"],"") & filters.private & devs, group = 2)
async def dev_source(c,msg):
    if msg.text == "• المطور الاول •":
        user_id = "@x_hseein"
    else:
        user_id = "@X_zazthon"
    user = await c.get_users(user_id)
    text = f"<b>• 𝖭𝖺𝗆𝖾 : {user.mention}</b>\n<b>• 𝗂𝖣 : {user_id}</b>"
    if user.username:
        text += f"\n<b>• 𝖴𝗌𝖾r : @{user.username}</b>"
    chat = await c.get_chat(user_id)
    if chat.bio:
        text += f"\n<b>•𝖡𝗂𝗈 :{chat.bio}</b>"
    if user.photo:
        async for photo in app.get_chat_photos(user_id,limit=1):
            await msg.reply_photo(photo.file_id, caption=text)
    else:
        await msg.reply(text)

@app.on_message(filters.command(["• اعادة التشغيل •"],"") & filters.private & devs, group = 2)
async def restart_(c,msg):
    response = await msg.reply_text("<b>جاري اعادة التشغيل...</b>")
    ac_chats = await get_active_chats()
    for x in ac_chats:
        try:
            await remove_active_chat(x)
            await remove_active_video_chat(x)
        except:
            pass

    try:
        shutil.rmtree("downloads")
        shutil.rmtree("raw_files")
        shutil.rmtree("cache")
    except:
        pass
    await response.edit_text(
        "• جاري تشغيل البوت خلال عدة ثواني ◟"
    )
    os.system(f"kill -9 {os.getpid()} && bash start")

@app.on_message(filters.command(["• للجروبات •","• للمستخدمين •","• للقنوات •"],"") & filters.private & devs, group = 2)
async def broadcast_gr(c,msg):
    try:
        m = await c.ask(msg.chat.id, "• قم بارسال الرسالة التي تريد نشرها ◟")
        if m.text in ["• للجروبات •" ,"• للمستخدمين •", "• للقنوات •"]:
            m = await c.ask(msg.chat.id, "•عذرا قم بارسال الرسالة التي تريد نشرها ◟")
        if msg.text == "• للجروبات •":
            chats = await get_served_chats() 
        else:
            chats = await get_served_users() if msg.text == "• للمستخدمين •" else await get_served_channel()
        x = 0
        n = "user_id" if msg.text == "• للمستخدمين •" else "chat_id"
        for chat in chats:
            try:
                if m.photo:
                    photo = await m.download()
                    await app.send_photo(int(chat[n]), photo=photo, caption=m.caption)
                elif m.video:
                    video = await m.download()
                    thumb = await app.download_media(m.video.thumbs[0].file_id)
                    await app.send_video(int(chat[n]), photo=video, caption=m.caption, duration=m.video.duration,thumb=thumb)
                else:
                    await app.send_message(int(chat[n]), text=m.text)
                x += 1
                await asyncio.sleep(0.2)
            except:
                pass
        if msg.text == "• للجروبات •":
            type = "جروب"  
        else:
            type = "مستخدم" if msg.text == "• للمستخدمين •" else "قناة"
        await msg.reply(f"• تم ارسال الى {x} {type}")
    except Exception as e:
        await msg.reply(f"- حدث خطا -> {e}")    

@app.on_message(filters.command(["• بالتوجيه للجروبات •", "• بالتوجيه للمستخدمين •","• بالتوجيه للقنوات •"],"") & filters.private & devs, group = 2)
async def broadcast_fr(c,msg):
    try:
        m = await c.ask(msg.chat.id, "• قم بارسال الرسالة التي تريد نشرها ◟")
        if m.text in ["• بالتوجيه للجروبات •", "• بالتوجيه للمستخدمين •","• بالتوجيه للقنوات •"]:
            m = await c.ask(msg.chat.id, "•عذرا قم بارسال الرسالة التي تريد نشرها ◟")
        if msg.text == "• بالتوجيه للجروبات •":
            chats = await get_served_chats() 
        else:
            chats = await get_served_users() if msg.text == "• بالتوجيه للمستخدمين •" else await get_served_channel()
        x = 0
        n = "user_id" if msg.text == "• بالتوجيه للمستخدمين •" else "chat_id"
        for chat in chats:
            try:
                await m.forward(int(chat[n]))
                x += 1
                await asyncio.sleep(0.2)
            except:
                pass
        if msg.text == "• بالتوجيه للجروبات •":
            type = "جروب"  
        else:
            type = "مستخدم" if msg.text == "• بالتوجيه للمستخدمين •" else "قناة"
        await msg.reply(f"• تم ارسال الى {x} {type}")
    except Exception as e:
        await msg.reply(f"- حدث خطا -> {e}")    

@app.on_message(filters.command(["• ترويج البوت •"],"") & filters.private & devs, group = 2)
async def broadcast_bot_(c,msg):
    try:
        owner = await c.get_users(int(OWNER_ID))
        text = f"<b>• بوت ميوزك قنوات وجروبات ، البوت يعمل بسرعة وجودة خارقة ، بدون تهنيج ولا تقطيع لان البوت شغال علي سيرفر لوحدو◟</b>\n\n<b>• ارفع البوت فـ قناتك او جروبك وجرب سرعة البوت بنفسك وشوف المميزات◟</b>\n\n<b>• يوزر البوت : @{c.me.username} ◟ </b>\n<b>• يوزر المطور : @{owner.username if owner.username else owner.mention} ◟</b>"
        chats = await get_served_chats() 
        x = 0
        for chat in chats:
            try:
                await c.send_message(int(chat["chat_id"]),text, reply_markup=ikm([[ikb("𓏺 𝖺𝖣𝖣 𝖬𝖾 𝖳𝗈 𝖸𝗈𝗎𝗋 𝖦𝗋𝗈u𝗉𝗌 .", url=f"https://t.me/{app.username}?startgroup=true")]]))
                x += 1
                await asyncio.sleep(0.2)
            except Exception as e:
                pass
        await msg.reply(f"• تم ارسال الى {x} جروب")
        chats = await get_served_channel() 
        x = 0
        for chat in chats:
            try:
                await c.send_message(int(chat["chat_id"]),text, reply_markup=ikm([[ikb("𓏺 𝖺𝖣𝖣 𝖬𝖾 𝖳𝗈 𝖸𝗈𝗎𝗋 𝖦𝗋𝗈u𝗉𝗌 .", url=f"https://t.me/{app.username}?startgroup=true")]]))
                x += 1
                await asyncio.sleep(0.2)
            except Exception as e:
                pass
        await msg.reply(f"• تم ارسال الى {x} قناة")
        users = await get_served_users() 
        x = 0
        for chat in users:
            try:
                await c.send_message(int(chat["user_id"]),text, reply_markup=ikm([[ikb("𓏺 𝖺𝖣𝖣 𝖬𝖾 𝖳𝗈 𝖸𝗈𝗎𝗋 𝖦𝗋𝗈u𝗉𝗌 .", url=f"https://t.me/{app.username}?startgroup=true")]]))
                x += 1
                await asyncio.sleep(0.2)
            except Exception as e:
                pass
        await msg.reply(f"• تم ارسال الى {x} مستخدم")
    except Exception as e:
        await msg.reply(f"- حدث خطا -> {e}")
