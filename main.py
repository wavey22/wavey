import telebot
from telebot import types

API_TOKEN = '8054496771:AAFn0qTsUwnnGCppGjFXfXjVZtJwhsxzk0w'
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row("🎙 Записаться", "💰 Прайс", "🎧 Портфолио")
    markup.row("📍 Контакты", "❓ FAQ")
    bot.send_message(message.chat.id, 
        "Привет! Добро пожаловать в студию звукозаписи. Чем могу помочь?", reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def handle_all_messages(message):
    if message.text == "🎙 Записаться":
        bot.send_message(message.chat.id, "Чтобы записаться, напиши нам в Telegram: @your_studio_admin")
    elif message.text == "💰 Прайс":
        bot.send_message(message.chat.id, "Наши услуги:"
- Запись вокала: 2000₽/час
- Сведение: от 3000₽
- Мастеринг: от 2000₽")
    elif message.text == "🎧 Портфолио":
        bot.send_message(message.chat.id, "Слушай наши работы здесь:
https://t.me/your_portfolio_channel")
    elif message.text == "📍 Контакты":
        bot.send_message(message.chat.id, "Адрес: Москва, Примерная улица 10
Телефон: +7 (999) 123-45-67
Instagram: @your_studio_ig")
    elif message.text == "❓ FAQ":
        bot.send_message(message.chat.id, "Частые вопросы:
— Что брать с собой?
— Можно ли прийти с друзьями?
— Сколько длится сессия?")
    else:
        bot.send_message(message.chat.id, "Выберите опцию из меню ⬆️")

bot.infinity_polling()
