import os
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from dotenv import load_dotenv

# Загружаем переменные окружения
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Инициализируем бота и диспетчер
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

# Команда /start
@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    await message.reply("Привет! Я бот студии звукозаписи 🎧\nНапиши /help, чтобы узнать, что я умею.")

# Команда /help
@dp.message_handler(commands=['help'])
async def help_handler(message: types.Message):
    await message.reply("""Вот, что я умею:
🎵 /price — Прайс на услуги
📞 /contact — Контакты
📍 /location — Адрес студии""")

# Команда /price
@dp.message_handler(commands=['price'])
async def price_handler(message: types.Message):
    await message.reply("""🎚 Прайс на услуги:
- Запись: от 1500 руб
- Сведение (микс): от 2500 руб
- Мастеринг: от 2000 руб""")

# Команда /contact
@dp.message_handler(commands=['contact'])
async def contact_handler(message: types.Message):
    await message.reply("📞 Наши контакты:\nTelegram: @waveyrec\nInstagram: @wavey.rec")

# Команда /location
@dp.message_handler(commands=['location'])
async def location_handler(message: types.Message):
    await message.reply("📍 Мы находимся в Москве, рядом с метро XYZ. Уточни адрес у администратора.")

# Запуск бота
if name == '__main__':
    executor.start_polling(dp, skip_updates=True)
