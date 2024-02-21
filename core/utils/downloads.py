import os
from aiogram import Bot
from aiogram.fsm.context import FSMContext
from core.settings import settings


async def download(file_path, file_name, bot):
    await bot.download_file(
        file_path, f"{settings.bots.path_folder}\\{file_name}"
    )
