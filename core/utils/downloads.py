import os
from aiogram import Bot
from aiogram.types import Message
from core.settings import settings


async def download(message: Message, bot: Bot):
    doc = await bot.get_file(message.document.file_id)
    name_doc = message.document.file_name
    # file_path = doc.file_path
    await bot.download_file(
        doc.file_path, f"{settings.bots.path_folder}\\{name_doc}"
        # doc.file_path, destination=f"{pathfile}\\{name_doc}"
    )
