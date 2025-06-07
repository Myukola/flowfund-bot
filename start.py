
from aiogram import types, Dispatcher

async def start_handler(message: types.Message):
    await message.answer("Привіт! Це FlowFund Бот. Підключи свій TON-гаманець для участі.")

def register(dp: Dispatcher):
    dp.register_message_handler(start_handler, commands=["start"])
