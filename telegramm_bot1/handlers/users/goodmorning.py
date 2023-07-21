from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp

# Навчити додаток на словосполучення «Доброго ранку» відповідати «Доброго ранку, чим будеш снідати?»
# Та надіслати наступним повідомленням якийсь смішний стікер який у вас асоціюється зі сніданком 

@dp.message_handler(text='Доброго ранку')
async def goodmor(message: types.Message):
    await message.answer(text='Доброго ранку, чим будеш снідати?')
    await message.answer_sticker("CAACAgIAAxkBAAMYZLpE8K0FjAzVuo7iqktEd7RqtKUAArQVAAL8oklI5i36aOzdXzIvBA")