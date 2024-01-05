from aiogram import Bot
from aiogram.types import Message
import json


async def get_start(message: Message, bot: Bot):
    await message.answer(
        f"Hi {message.from_user.first_name}. It's good to see you!"
    )


async def get_photo(message: Message, bot: Bot):
    await message.answer(
        f"Exsellent. You sent the picture, I kept it for myself."
    )
    file = await bot.get_file(message.photo[-1].file_id)
    await bot.download_file(file.file_path, 'photo/photo.jpg')


async def get_hello(message: Message, bot: Bot):
    await message.answer(f"Hello to you!")
    json_str = json.dumps(message.dict(), default=str)
    print(json_str)