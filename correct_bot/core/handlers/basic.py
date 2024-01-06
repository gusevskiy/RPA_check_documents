from aiogram import Bot
from aiogram.types import Message
import json
from core.keyboards.reply import reply_keyboard, loc_tel_poll_keyboard, get_reply_keyboard
from core.keyboards.inline import select_macbook, get_inline_keyboard


async def get_inline(message: Message, bot: Bot):
    await message.answer(
        f"Hi, {message.from_user.first_name}. Showing inline buttons",
        # reply_markup=select_macbook
        reply_markup=get_inline_keyboard()
    )


async def get_start(message: Message, bot: Bot):
    await message.answer(
        f"Hi {message.from_user.first_name}. It's good to see you!",
        # select keyboard from keyboards/reply.py
        reply_markup=get_reply_keyboard()
    )


async def get_location(message: Message, bot: Bot):
    await message.answer(
        f"You send location!\r\a"
        f"{message.location.latitude}\r\n{message.location.longitude}"
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
