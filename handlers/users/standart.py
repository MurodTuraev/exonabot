from aiogram import types
from aiogram.types import InputFile
from loader import dp, bot
from keyboards.default.menuKeyboard import StandartBtn, CategoryBtn, ContactBtn
from keyboards.inline.checkout import Basic_1_kb, Vip_1_kb, Basic_2_kb, Vip_2_kb

@dp.message_handler(text="Standart")
async def bot_standart(message: types.Message):
    send_text = "<b>STANDART</b>\n" \
                "kategoriyasidagi barcha tariflar eng minimal imkoniyatlarga ega bo’lib, ular faqatgina boshqa shaxs mashinasiga yetkazilgan zararlarni qisman qoplash uchun xizmat qiladi."
    await message.answer(send_text, reply_markup=StandartBtn)

@dp.message_handler(text="Bosh menu")
async def bot_main(message: types.Message):
    await message.answer("Bosh menu bosildi", reply_markup=CategoryBtn)


@dp.message_handler(text="Basic 1")
async def bot_basic1(message: types.Message):
    basic_1 = InputFile(path_or_bytesio="tarif/standart/Basic1.png")
    await message.answer_photo(basic_1, reply_markup=Basic_1_kb)
    admin = 1002053862
    photo_url = "https://www.agros.uz/media/uploads/2022/02/17/basic1_XmAGjQB.png"
    await bot.send_photo(chat_id=admin, photo=photo_url, caption=f"@{message.from_user.username} - aloqaga chiqdi")

@dp.message_handler(text="VIP 1")
async def bot_vip_1(message: types.Message):
    vip_1 = InputFile(path_or_bytesio="tarif/standart/Vip1.png")
    await message.answer_photo(vip_1, reply_markup=Vip_1_kb)
    admin = 1002053862
    photo_url = "https://www.agros.uz/media/uploads/2022/02/17/vip1_gnoNwIQ.png"
    await bot.send_photo(chat_id=admin, photo=photo_url, caption=f"@{message.from_user.username} - aloqaga chiqdi")

@dp.message_handler(text="Basic 2")
async def bot_basic2(message: types.Message):
    basic_2 = InputFile(path_or_bytesio="tarif/standart/Basic2.png")
    await message.answer_photo(basic_2, reply_markup=Basic_2_kb)
    admin = 1002053862
    photo_url = "https://www.agros.uz/media/uploads/2022/02/17/basic2_KJzhXI2.png"
    await bot.send_photo(chat_id=admin, photo=photo_url, caption=f"@{message.from_user.username} - aloqaga chiqdi")


@dp.message_handler(text="VIP 2")
async def bot_vip_2(message: types.Message):
    vip_2 = InputFile(path_or_bytesio="tarif/standart/Vip2.png")
    await message.answer_photo(vip_2, reply_markup=Vip_2_kb)
    admin = 1002053862
    photo_url = "https://www.agros.uz/media/uploads/2022/02/17/vip2_PQAjbHw.png"
    await bot.send_photo(chat_id=admin, photo=photo_url, caption=f"@{message.from_user.username} - aloqaga chiqdi")

@dp.callback_query_handler(text="basic_1_doc")
async def basic_1_doc_call(callback: types.CallbackQuery):
    content = "<b>Siz 'Basic 1' tarifini tanladingiz polisni rasmiylashtirish uchun quyidagi hujjatlarni <b>admin</b>ga yuboring:</b>\n" \
              "1. Texnik pasport\n" \
              "2. Pasportlar \n" \
              "3. Haydovchilik guvohnamalar\n\n"


    await callback.message.answer(text=content)
    to_admin = "Admin: @exona_admin"
    await callback.message.answer(to_admin)
    await callback.answer()



@dp.callback_query_handler(text="vip_1_doc")
async def vip_1_doc_call(callback: types.CallbackQuery):
    content = "<b>Siz 'Vip 1' tarifini tanladingiz polisni rasmiylashtirish uchun quyidagi hujjatlarni <b>admin</b>ga yuboring:</b>\n" \
              "1. Texnik pasport\n" \
              "2. Pasportlar \n " \
              "3. Haydovchilik guvohnamalar\n\n"

    await callback.message.answer(content)
    to_admin = "Admin: @exona_admin"
    await callback.message.answer(to_admin)
    await callback.answer()


@dp.callback_query_handler(text="basic_2_doc")
async def basic_2_doc_call(callback: types.CallbackQuery):
    content = "<b>Siz 'Basic 2' tarifini tanladingiz polisni rasmiylashtirish uchun quyidagi hujjatlarni <b>admin</b>ga yuboring:</b>\n" \
              "1. Texnik pasport\n" \
              "2. Pasportlar \n" \
              "3. Haydovchilik guvohnamalar\n\n"

    await callback.message.answer(content)
    to_admin = "Admin: @exona_admin"
    await callback.message.answer(to_admin)
    await callback.answer()




@dp.callback_query_handler(text="vip_2_doc")
async def vip_2_doc_call(callback: types.CallbackQuery):
    content = "<b>Siz 'Vip 2' tarifini tanladingiz polisni rasmiylashtirish uchun quyidagi hujjatlarni <b>admin</b>ga yuboring:</b>\n" \
              "1. Texnik pasport\n" \
              "2. Pasportlar \n" \
              "3. Haydovchilik guvohnamalar\n\n"

    await callback.message.answer(content)
    to_admin = "Admin: @exona_admin"
    await callback.message.answer(to_admin)
    await callback.answer()

