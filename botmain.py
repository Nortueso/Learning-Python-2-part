# NEW
import telebot
from datetime import datetime
import os
TOKEN = "8592926270:AAHQeHn7sI4wHCfHh8zE7UrgshVowhHBp6s"
bot = telebot.TeleBot(TOKEN)
bot.polling(none_stop=True)
bot.remove_webhook()
import time
import requests
from dotenv import load_dotenv
load_dotenv()
from apscheduler.schedulers.background import BackgroundScheduler


@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.reply_to(message, "Hello, type to me word 'Time', then ill tell you how much time." )

@bot.message_handler(content_types=["text"])
def  get_text_message(message):
    chat_id = message.chat.id
    text = message.text.lower()
    
    if message.text.lower() == "time":
        current_time = datetime.now().strftime("%H:%M:%S")
        bot.send_message(message.from_user.id, f"🕒 Текущее время: {current_time}" )
    
    elif text == "поставить будильник":
    # Создаем inline-кнопки под сообщением для выбора времени
        inline_markup = telebot.types.InlineKeyboardMarkup()
        btn_10s = telebot.types.InlineKeyboardButton("Через 10 сек", callback_data="alarm_10")
        btn_1m = telebot.types.InlineKeyboardButton("Через 1 мин", callback_data="alarm_60")
        inline_markup.add(btn_10s, btn_1m)
        bot.send_message(chat_id, "Через какое время запустить будильник?", reply_markup=inline_markup)
    
    else:
        bot.send_message(message.from_user.id, "I can show only time, print 'time'")



# Обработка нажатий на инлайн-кнопки (выбор времени будильника)
@bot.callback_query_handler(func=lambda call: call.data.startswith('alarm_'))
def callback_alarm(call):
    chat_id = call.message.chat.id
    # Извлекаем количество секунд (10 или 60) из нажатой кнопки
    seconds = int(call.data.split('_')[1])
    
    # Считаем точное время, когда должен сработать будильник
    from datetime import timedelta
    run_time = datetime.now() + timedelta(seconds=seconds)
    
    # Добавляем задачу в планировщик на выполнение в конкретное время (тип 'date')
    scheduler.add_job(send_alarm, 'date', run_date=run_time, args=[chat_id])
    
    # Обновляем текст кнопки в Telegram, подтверждая установку
    bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id, 
                                            text=f"✅ Будильник успешно установлен на {seconds} секунд!")




# reminder
scheduler = BackgroundScheduler()
scheduler.start()

def send_alarm(chat_id):
    bot.send_message(chat_id, "⏰ БУДИЛЬНИК! Время пришло! Срочно просыпайся/сделай перерыв!")

# Запуск бота в бесконечном режиме ожидания сообщений
print("Бот запущен и готов к работе...")
while True:
    try:
        bot.polling(none_stop=True, interval=0, timeout=90, long_polling_timeout=90)
    except (requests.exceptions.ConnectionError, Exception) as e:
        print(f"Произошел сбой сети: {e}. Переподключение через 5 секунд...")
        time.sleep(5)


