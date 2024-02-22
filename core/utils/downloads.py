import os
from aiogram import Bot
from aiogram.fsm.context import FSMContext
from core.settings import settings


async def download(file_path, file_name, bot):
    # print(file_path)
    await bot.download_file(
        file_path, f"{settings.bots.path_folder}\\{file_name}"
    )


async def delete_file():
    """
    Удаляет все файлы из папки doc.
    """
    for filename in os.listdir(settings.bots.path_folder):
        os.remove(settings.bots.path_folder + "\\" + filename)
