import aiogram.utils.markdown as fmt
from aiogram import types
from loader import dp, bot
from aiogram.types import InputFile


@dp.message_handler(commands="afisha")
async def with_hidden_link(message: types.Message):


    reklama_photo = InputFile(path_or_bytesio="tarif/afisha/reklama.jpg")


    reklama_text = f"Endi <b>SUG‘URTA POLISLAR</b>ni telefoningiz yordamida rasmiylashtirishingiz mumkin!\n"\
                    f"Sizlarga mamnuniyat bilan shuni ma’lum qilamizki, transport vositasi uchun sug‘urta polisini <a href='@exona_bot'><b>“Exona bot”</b> </a>  orqali istalgan vaqtda sotib olishingiz mumkin!\n\n"\
                    f"<b>“Exona Bot”</b>da quyidagi qulayliklar mavjud:\n\n"\
                    f"🚘 Avtosug‘urta polislarni onlayn xarid qilish\n"\
                    f"📅 Haftada 7 kun, sutkada 24 soat davomida xizmat ko‘rsatish\n"\
                    f"💰 Payme/Click/Plastik kartaga pul o‘tkazish orqali to‘lovni amalga oshirish\n\n"\
                    f"Qo‘shimcha ma’lumot uchun:\n"\
                    f"☎️ +99891 001 24 41\n"\
                    f"🌐 http://exona.uz\n"\
                    f"📩 info@exona.uz\n"\
                    f"🤖 @exona_admin\n\n"\
                    f"Sug‘urta polisini xarid qilish: @exona_bot\n"



    await message.answer_photo(reklama_photo, caption=reklama_text, parse_mode='html')