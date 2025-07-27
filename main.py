import os
import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.enums import ParseMode
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from aiogram.client.default import DefaultBotProperties
from dotenv import load_dotenv

# Загружаем токен из .env
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Инициализируем бота и диспетчер
bot = Bot(
    token=BOT_TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)
dp = Dispatcher()

# Обработчики
@dp.message(CommandStart())
async def start_handler(message: Message):
    await message.answer("Привет! Я бот студии звукозаписи 🎧\nНапиши /help, чтобы узнать, что я умею.")

@dp.message(Command("help"))
async def help_handler(message: Message):
    await message.answer("""Вот, что я умею:
🎵 /price — Прайс на услуги
📞 /contact — Контакты
📍 /location — Адрес студии""")

@dp.message(Command("price"))
async def price_handler(message: Message):
    await message.answer("""🎚 <b>Прайс на услуги:</b>
- Запись: от 1500 руб
- Сведение (микс): от 2500 руб
- Мастеринг: от 2000 руб""")

@dp.message(Command("contact"))
async def contact_handler(message: Message):
    await message.answer("📞 Наши контакты:\nTelegram: @waveyrec\nInstagram: @wavey.rec")

@dp.message(Command("location"))
async def location_handler(message: Message):
    await message.answer("📍 Мы находимся в Москве, рядом с метро XYZ. Уточни адрес у администратора.")

# Запуск
async def main():
    await dp.start_polling(bot)

if name == "__main__":
    asyncio.run(main())
