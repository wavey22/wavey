import os
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import CommandStart
from aiogram.client.default import DefaultBotProperties
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(
    token=BOT_TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)
dp = Dispatcher()

# Главное меню
main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🎧 Услуги")],
        [KeyboardButton(text="🎚 Звукооператор")],
        [KeyboardButton(text="👤 Администратор")],
        [KeyboardButton(text="📞 Контакты"), KeyboardButton(text="📍 Адрес студии")],
    ],
    resize_keyboard=True
)

# Меню услуг
service_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🎙 Запись"), KeyboardButton(text="🎚 Сведение")],
        [KeyboardButton(text="🥁 Бит"), KeyboardButton(text="➕ Дополнительные услуги")],
        [KeyboardButton(text="⬅ Назад в меню")],
    ],
    resize_keyboard=True
)

# Звукооператоры
operator_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🎛 Макар"), KeyboardButton(text="🎛 Иван")],
        [KeyboardButton(text="⬅ Назад")],
    ],
    resize_keyboard=True
)

@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(
        "Добро пожаловать в студию WAVEY 🎙\nВыберите действие из меню ниже:",
        reply_markup=main_menu
    )

@dp.message()
async def handle_buttons(message: Message):
    text = message.text

    if text == "🎧 Услуги":
        await message.answer("Выберите нужную услугу:", reply_markup=service_menu)

    elif text == "🎙 Запись":
        await message.answer(
            "🎙 <b>Запись</b>: от 500₽\n\nВыберите звукооператора:", reply_markup=operator_menu
        )

    elif text == "🎚 Сведение":
        await message.answer(
            "🎚 <b>Сведение</b>: от 3000₽\n\nВыберите звукооператора:", reply_markup=operator_menu
        )

    elif text == "🥁 Бит":
        await message.answer(
            "🥁 <b>Бит</b>: от 3000₽\n\nВыберите звукооператора:", reply_markup=operator_menu
        )

    elif text == "➕ Дополнительные услуги":
        await message.answer(
            "Для обсуждения дополнительных услуг свяжитесь с администратором: @AttaRaxOnMe"
        )

    elif text == "📞 Контакты":
        await message.answer("📲 Наши контакты:\nTelegram: @WAVEY_SOUND")

    elif text == "📍 Адрес студии":
        await message.answer(
            "🏢 Мы находимся в г. Ростов-на-Дону\n📍 Адрес: ул. Михаила Нагибина, 14Г"
        )

    elif text == "🎚 Звукооператор":
        await message.answer("Выберите звукооператора:", reply_markup=operator_menu)

    elif text == "🎛 Макар":
        await message.answer(
            "🎛 Вы выбрали звукорежиссёра Макар.\nСвяжитесь с ним: @CYStnzo"
        )

    elif text == "🎛 Иван":
        await message.answer(
            "🎛 Вы выбрали звукорежиссёра Иван.\nСвяжитесь с ним: @aa_ladno"
        )

    elif text == "👤 Администратор":
        await message.answer("👤 Администратор студии: @AttaRaxOnMe")

    elif text == "⬅ Назад" or text == "⬅ Назад в меню":
        await message.answer("Главное меню:", reply_markup=main_menu)

    else:
        await message.answer("Выберите действие через меню снизу 👇")

# Запуск
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
