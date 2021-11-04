@pyrogram.Client.on_message(pyrogram.filters.text)
async def rename_doc(bot, update):
    m = update.text
    try:
        await bot.get_chat_member('@SH_Bots',update.chat.id)
        await bot.get_chat_member('@pscplusIN',update.chat.id)
    except:
        await bot.send_message(
            text= "Please Join @SH_Bots & @pscplusIN To Use This Bot",
            chat_id=update.chat.id
        )
        return
    if not m.startswith("/"):
        s = pyqrcode.create(m)
        s.png('generated.png', scale = 6)
        await bot.send_photo(
            chat_id=update.chat.id,
            photo="generated.png"
        )
    else:
        await bot.send_message(
            text= "Sent A Text Or Link To Convert To Qr Code",
            chat_id=update.chat.id,
            reply_markup=InlineKeyboardMarkup(
               [
                    [InlineKeyboardButton('✅ SHARE BOT ✅', url='https://t.me/share/url?url=https://t.me/Qrcode_gen_bot')],
               ]
            )
        )
