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


# async def get_document(message: Message, bot: Bot):
#     size_doc = message.document.file_size
#     if size_doc < 90000:
#         doc = await bot.get_file(message.document.file_id)
#         name_doc = message.document.file_name
#         await bot.download_file(
#             doc.file_path, f"{settings.bots.path_folder}\\{name_doc}"
#         )
#     else:
#         await message.answer(
#             f"Документ {message.document.file_name} слишком большой возможно это не <b>Акт сверки!</b>"
#         )
