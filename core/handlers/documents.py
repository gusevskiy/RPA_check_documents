import os
import pathlib
from collections import Counter
from aiogram import Bot
from core.settings import settings
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from core.utils.statedocuments import StepsDocuments
from core.utils.downloads import download_file, delete_file
from core.processing import work


async def check_state(message: Message, bot: Bot, state: FSMContext):
    file_pdf = ""
    file_xlsx = ""
    folder = settings.bots.path_folder
    data = await state.get_data()
    for i in os.listdir(folder):
        if i.endswith(".pdf"):
            file_pdf = f"{folder}\\{i}"
        if i.endswith(".xlsx"):
            file_xlsx = f"{folder}\\{i}"
    work.work_main(file_pdf, file_xlsx)
    # print(file_pdf)
    # file_pdf = (await bot.get_file(data['file_pdf']["file_id"])).file_path
    # file_xlsx = (await bot.get_file(data['file_xlsx']["file_id"])).file_path

    # data = await state.get_data()
    # print(data)


async def get_document(message: Message, bot: Bot, state: FSMContext):
    list_extension = [".pdf", ".xlsx"]
    if message.document:
        if pathlib.Path(message.document.file_name).suffix in list_extension:
            file_path = (await bot.get_file(message.document.file_id)).file_path
            file_info = {
                "file_id": message.document.file_id,
                "file_name": message.document.file_name,
                "file_path": file_path
            }
            user_data = await state.get_data()  # Получаем текущий список файлов из состояния
            files = user_data.get("documents", [])
            files.append(file_info)  # Добавляем информацию о новом файле
            await state.update_data(documents=files)  # Обновляем состояние с новым списком файлов
        else:
            await message.answer(f"Разрешение файла {message.document.file_name} НЕ принимается.")
    data = await state.get_data()
    if data.get("documents") and len(data["documents"]) == 2:
        for i in data["documents"]:
            key_path = i["file_path"]
            key_name = i["file_name"]
            await download_file(key_path, key_name, bot)


async def req_document(message: Message, state: FSMContext):
    await delete_file()
    await state.clear()
    await message.reply(f"{message.from_user.first_name} Присылай файлы!")
    await state.set_state(StepsDocuments.GET_DOCUMENT)
