
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils import executor
import os
from handlers import start, wallet

bot = Bot(token=os.getenv("BOT_TOKEN"))
dp = Dispatcher(bot)

start.register(dp)
wallet.register(dp)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
