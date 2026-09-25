#1----------> libs/modules st
import aiogram
import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
#1----------> libs/modules fn

#2----------> logging for errors st
logging.basicConfig(level = logging.INFO)
#2----------> logging for errors fn

#3----------> bot settings st 
TOKEN="8592926270:AAHQeHn7sI4wHCfHh8zE7UrgshVowhHBp6s"
bot = Bot(token=TOKEN)
dp = Dispatcher()
#3----------> bot setting fn

#4----------> command /start st
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(" WSP ")
#4----------> command /start fn

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())