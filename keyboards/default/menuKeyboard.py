from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

CategoryBtn = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Standart'),
            KeyboardButton(text='Premium'),
        ],
    ],
    resize_keyboard=True
)

PremiumBtn = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Basic 1+'),
            KeyboardButton(text='VIP 1+'),
        ],
        [
            KeyboardButton(text='Basic 2+'),
            KeyboardButton(text='VIP 2+'),
        ],
        [
            KeyboardButton(text='Bosh menu'),
        ],
    ],
    resize_keyboard=True
)

StandartBtn = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Basic 1'),
            KeyboardButton(text='VIP 1'),
        ],
        [
            KeyboardButton(text='Basic 2'),
            KeyboardButton(text='VIP 2'),
        ],
        [
            KeyboardButton(text='Bosh menu'),
        ],
    ],
    resize_keyboard=True
)

ContactBtn = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('Telefon raqamni yuborish ☎️', request_contact=True)
        ],
    ],
    resize_keyboard=True
)



