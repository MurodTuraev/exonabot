# User_ids
# shaxzodbek = 591435940
# beeline = 1002053862

from aiogram import types
from aiogram.types import InputFile
from loader import dp, bot
from keyboards.default.menuKeyboard import PremiumBtn, CategoryBtn, ContactBtn
from keyboards.inline.checkout import Basic_1_plus_kb, Vip_1_plus_kb, Basic_2_plus_kb, Vip_2_plus_kb


@dp.message_handler(text="Premium")
async def bot_premium(message: types.Message):
    send_text = "<b>PREMIUM</b>\n " \
                "kategoriyasidagi barcha tariflar haydovchining sog‘lig‘iga yetkazilgan zararlarni qoplash uchun xizmat qiladi."
    await message.answer(send_text, reply_markup=PremiumBtn)


@dp.message_handler(text="Bosh menu")
async def bot_main(message: types.Message):
    await message.answer("Bosh menu bosildi", reply_markup=CategoryBtn)


@dp.message_handler(text="Basic 1+")
async def bot_basic_1_plus(message: types.Message):
    basic_1_plus = InputFile(path_or_bytesio="tarif/premium/Basic1+.png")
    await message.answer_photo(basic_1_plus, reply_markup=Basic_1_plus_kb)
    admin = 1002053862
    photo_url = "https://www.agros.uz/media/uploads/2022/02/17/basic1.png"
    await bot.send_photo(chat_id=admin, photo=photo_url, caption=f"@{message.from_user.username} - aloqaga chiqdi")


@dp.message_handler(text="VIP 1+")
async def bot_vip_1_plus(message: types.Message):
    vip_1_plus = InputFile(path_or_bytesio="tarif/premium/Vip1+.png")
    await message.answer_photo(vip_1_plus, reply_markup=Vip_1_plus_kb)
    admin = 1002053862
    photo_url = "https://www.agros.uz/media/uploads/2022/02/17/vip1.png"
    await bot.send_photo(chat_id=admin, photo=photo_url, caption=f"@{message.from_user.username} - aloqaga chiqdi")


@dp.message_handler(text="Basic 2+")
async def bot_basic_2_plus(message: types.Message):
    basic_2_plus = InputFile(path_or_bytesio="tarif/premium/Basic2+.png")
    await message.answer_photo(basic_2_plus, reply_markup=Basic_2_plus_kb)
    admin = 1002053862
    photo_url = "https://www.agros.uz/media/uploads/2022/02/17/basic2.png"
    await bot.send_photo(chat_id=admin, photo=photo_url, caption=f"@{message.from_user.username} - aloqaga chiqdi")


@dp.message_handler(text="VIP 2+")
async def bot_vip_2_plus(message: types.Message):
    vip_2_plus = InputFile(path_or_bytesio="tarif/premium/Vip2+.png")
    await message.answer_photo(vip_2_plus, reply_markup=Vip_2_plus_kb)
    admin = 1002053862
    photo_url = "https://www.agros.uz/media/uploads/2022/02/17/vip2.png"
    await bot.send_photo(chat_id=admin, photo=photo_url, caption=f"@{message.from_user.username} - aloqaga chiqdi")


@dp.callback_query_handler(text="basic_1_plus_doc")
async def basic_1_plus_doc_call(callback: types.CallbackQuery):
    content = "<b>Siz 'Basic 1 + ' tarifini tanladingiz  polisni rasmiylashtirish uchun quyidagi hujjatlarni <b>admin</b>ga yuboring</b>\n" \
              "1. Texnik pasport\n" \
              "2. Pasportlar \n " \
              "3. Haydovchilik guvohnamalar\n\n" 
    
    await callback.message.answer(content)
    to_admin = "Admin: @exona_admin"
    await callback.message.answer(to_admin)
    await callback.answer()




@dp.callback_query_handler(text="vip_1_plus_doc")
async def vip_1_plus_doc_call(callback: types.CallbackQuery):
    content = "<b>Siz 'Vip 1 + ' tarifini tanladingiz  polisni rasmiylashtirish uchun quyidagi hujjatlarni <b>admin</b>ga yuboring</b>\n" \
              "1. Texnik pasport\n" \
              "2. Pasportlar \n " \
              "3. Haydovchilik guvohnamalar\n\n"
    
    await callback.message.answer(content)
    to_admin = "Admin: @exona_admin"
    await callback.message.answer(to_admin)
    await callback.answer()



@dp.callback_query_handler(text="basic_2_plus_doc")
async def basic_2_plus_doc_call(callback: types.CallbackQuery):
    content = "<b>Siz 'Basic 2 + ' tarifini tanladingiz  polisni rasmiylashtirish uchun quyidagi hujjatlarni <b>admin</b>ga yuboring</b>\n" \
              "1. Texnik pasport\n" \
              "2. Pasportlar \n " \
              "3. Haydovchilik guvohnamalar\n\n" 
    
    await callback.message.answer(content)
    to_admin = "Admin: @exona_admin"
    await callback.message.answer(to_admin)
    await callback.answer()


@dp.callback_query_handler(text="vip_2_plus_doc")
async def vip_2_plus_doc_call(callback: types.CallbackQuery):
    content = "<b>Siz 'Vip 2 + ' tarifini tanladingiz  polisni rasmiylashtirish uchun quyidagi hujjatlarni <b>admin</b>ga yuboring</b>\n" \
              "1. Texnik pasport\n" \
              "2. Pasportlar \n " \
              "3. Haydovchilik guvohnamalar\n\n" 
    
    await callback.message.answer(content)
    to_admin = "Admin: @exona_admin"
    await callback.message.answer(to_admin)
    await callback.answer()

