from aiogram import Bot
import logging
from aiogram.types import Message
from core.utils.downloads import download
from core.settings import settings


async def get_start(message: Message, bot: Bot):
    await message.answer(
        f"<b>Привет {message.from_user.first_name}. Рад тебя видеть!</b>"
    )
    await message.answer(
        f"посмотреть инструкцию можно нажав кнопку Меню и выбрав /help"
    )


async def response_to_test(message: Message, bot: Bot):
    await message.answer("НУ чего ты мне пишешь?")


async def instruction(message: Message, bot: Bot):
    await message.answer("Принцип работы робота, следующий.")