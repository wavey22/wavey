import os
import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.enums import ParseMode
from aiogram.types import Message, KeyboardButton, ReplyKeyboardMarkup
from aiogram.filters import CommandStart
from aiogram.client.default import DefaultBotProperties
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()

# Звукооператоры Telegram user_id
MAKAR_ID = 864755307
IVAN_ID = 536852886

# Глобальные переменные для текущего выбора
user_states = {}

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

# Меню выбора услуг
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

# Кнопка записаться
confirm_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📩 Записаться")],
        [KeyboardButton(text="⬅ Назад в меню")],
    ],
    resize_keyboard=True
)

@dp.message(CommandStart())
async def start_cmd(message: Message):
    await message.answer(
        "Добро пожаловать в студию WAVEY 🎙\nВыберите действие из меню ниже:",
        reply_markup=main_menu
    )

@dp.message(F.text == "🎧 Услуги")
async def choose_service(message: Message):
    await message.answer("Выберите услугу:", reply_markup=service_menu)

@dp.message(F.text == "🎙 Запись")
async def service_record(message: Message):
    user_states[message.from_user.id] = {'service': 'Запись'}
    await message.answer("🎙 <b>Запись</b>: от 500₽\nВыберите звукорежиссёра:", reply_markup=operator_menu)

@dp.message(F.text == "🎚 Сведение")
async def service_mix(message: Message):
    user_states[message.from_user.id] = {'service': 'Сведение'}
    await message.answer("🎚 <b>Сведение</b>: от 3000₽\nВыберите звукорежиссёра:", reply_markup=operator_menu)

@dp.message(F.text == "🥁 Бит")
async def service_beat(message: Message):
    user_states[message.from_user.id] = {'service': 'Бит'}
    await message.answer("🥁 <b>Бит</b>: от 3000₽\nВыберите звукорежиссёра:", reply_markup=operator_menu)

@dp.message(F.text == "➕ Дополнительные услуги")
async def extra_services(message: Message):
    await message.answer("Для обсуждения дополнительных услуг свяжитесь с администратором: @AttaRaxOnMe")

@dp.message(F.text == "🎛 Макар")
async def choose_makar(message: Message):
    user_states[message.from_user.id]['operator'] = 'Макар'
    await message.answer("Вы выбрали звукооператора: Макар\nНажмите 📩 Записаться, чтобы отправить заявку", reply_markup=confirm_menu)

@dp.message(F.text == "🎛 Иван")
async def choose_ivan(message: Message):
    user_states[message.from_user.id]['operator'] = 'Иван'
    await message.answer("Вы выбрали звукооператора: Иван\nНажмите 📩 Записаться, чтобы отправить заявку", reply_markup=confirm_menu)

@dp.message(F.text == "📩 Записаться")
async def confirm_booking(message: Message):
    data = user_states.get(message.from_user.id)
    if not data or 'service' not in data or 'operator' not in data:
        await message.answer("Сначала выберите услугу и звукорежиссёра.")
        return

    operator = data['operator']
    service = data['service']
    username = message.from_user.username or message.from_user.full_name

    text = f"⚡️ Новый клиент @{username} хочет записаться на услугу: <b>{service}</b>"

    if operator == "Макар":
        await bot.
