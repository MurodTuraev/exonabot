from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp, bot
from filters import IsPrivate
from keyboards.default.menuKeyboard import CategoryBtn, StandartBtn, PremiumBtn, ContactBtn

@dp.message_handler(IsPrivate(), CommandStart())
async def bot_start(message: types.Message):

    send_text = f"Salom, <b>{message.from_user.full_name}</b>\n"\
                f"<i>sug‘urta polisini rasmiylashtirish uchun bizga telefon raqamingizni yuboring</i> ⤵️"



    await message.answer(send_text, parse_mode='html', reply_markup=ContactBtn)

@dp.message_handler(content_types=['contact'])
async def contact(message):
    if message.contact is not None:
        keyboard2 = types.ReplyKeyboardRemove()
        send_text = f"Telefon raqamingiz qabul qilindi\n\n" \
                    f"Tarifni tanlang"

        await bot.send_message(message.chat.id, text=send_text, reply_markup=CategoryBtn)
        global phonenumber
        phonenumber= str(message.contact.phone_number)
        user_id = str(message.contact.user_id)
        print(phonenumber)
