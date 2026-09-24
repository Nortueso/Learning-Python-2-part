# NEW
import telebot
from datetime import datetime
TOKEN = "8592926270:AAFNxfWoBIjSRbBCVKotze9_d9lKvwVEr8A"
bot = telebot.TeleBot(TOKEN)
@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.reply_to(message, "Hello, type to me word 'Time', then ill tell you how much time." )
@bot.message_handler(content_types=["text"])

def  get_text_message(message):
    if message.text.lower() == "time":
        current_time = datetime.now().strftime("%H:%M:%S")
        bot.send_message(message.from_user.id, f"🕒 Текущее время: {current_time}" )
    else:
        bot.send_message(message.from_user.id, "I can show only time, print 'time'")
print("Bot is turned on & ready to working...")
# Удаляем вебхук, чтобы сбросить конфликт 409
bot.remove_webhook()

# Запуск бота в бесконечном режиме ожидания сообщений
print("Бот запущен и готов к работе...")
bot.polling(none_stop=True)


