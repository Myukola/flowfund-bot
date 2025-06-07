
from aiogram import types, Dispatcher

async def wallet_handler(message: types.Message):
    await message.answer("Тут буде логіка перевірки транзакції FFU. Поки що демо.")

def register(dp: Dispatcher):
    dp.register_message_handler(wallet_handler, commands=["wallet"])
