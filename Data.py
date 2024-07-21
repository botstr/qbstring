from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
**❄️ مرحـبـاً** {},
━━━━━━━━━━━━━━━━━━━━━━━━
**- في البوت الرسـمي التابـع لـ سـورس** 𝙕𝞝𝘿𝙏𝙃𝙊𝙉 🤖🦾
**- لاستخراج كود تيرمكس وانشـاء جلسـة البـوت**
━━━━━━━━━━━━━━━━━━━━━━━━
**- قم بالضغط ع بـدء انشـاء جلسـه واتبـع التعليمـات 🛂**
━━━━━━━━━━━━━━━━━━━━━━━━
**- ملاحظـات هامـه :
• لا تقم بمشـاركة الكـود المستخـرج مع اي حـدا ⚠️**
**• لا تقم بطـرد جلسـة البـوت بعـد استخـراج الكـود 🚸**
━━━━━━━━━━━━━━━━━━━━━━━━
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("بـدء انشـاء جلسـة البـوت", callback_data="generate")],
        [InlineKeyboardButton(text=" رجــوع ", callback_data="home")],
    ]

    generate_button = [
        [InlineKeyboardButton("بـدء انشـاء جلسـة البـوت", callback_data="generate")]
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("بـدء انشـاء جلسـة البـوت", callback_data="generate")],
        [
            InlineKeyboardButton("مسـاعدة", callback_data="help"),
            InlineKeyboardButton("حول البوت", callback_data="about"),
        ],
    ]

    # Help Message
    HELP = """
**- اوامـر البـوت الاخـرى ⌨:**

/about - حـول البـوت
/help - اوامـر المسـاعده
/start - بـدء تشغيـل البـوت
/generate - بـدء انشـاء جلسـه
/cancel - الغـاء
/restart - اعـادة تشغيـل
"""

    # About Message
    ABOUT = """
**- حــول البـــوت :**

**» بـوت انشـاء جلسـة البـوت واستخـراج كـود تيرمكـس التابـع لســورس زدثـــون .. مبني ع آخـر اصـدار لـ لغـة بايثـون 3.9.7** 🌐🦾
    
**» لغة البوت 🅿️:** [Python³](https://www.python.org/)

**» مطور البـوت 🧑🏻‍💻:** [✵࿆• 𝙕 .࿆𝜜 .࿆𝙕 •✵࿆](https://t.me/ZlZZl77)

**» قناة السورس 🌐:** [𝙕𝙚𝙙𝙏𝙝𝙤𝙣](https://t.me/Zedthon)

**» الشـروحـات 🛂:** 
- [شروحات تنصيب 𝙕𝙚𝙙𝙏𝙝𝙤𝙣](https://t.me/zzzlvv)
- [شروحات تنصيب 𝙕𝙚𝙙𝙏𝙝𝙤𝙣 عبـر البـوت](https://t.me/W_l_N)

    """
