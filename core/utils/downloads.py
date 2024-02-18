import os
from aiogram import Bot
from aiogram.fsm.context import FSMContext
from core.settings import settings


async def download(bot: Bot, state: FSMContext):
    data = await state.get_data()
    files_info = data.get('files_info', [])
    for i in files_info:
        file_id = i["file_id"]
        file_name = i["file_name"]
        doc = await bot.get_file(file_id)
        await bot.download_file(
            doc.file_path, f"{settings.bots.path_folder}\\{file_name}"
            # doc.file_path, destination=f"{pathfile}\\{name_doc}"
        )
