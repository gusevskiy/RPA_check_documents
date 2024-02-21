import os
from collections import Counter
from aiogram import Bot
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from core.utils.statedocuments import StepsDocuments
from core.utils.downloads import download
from core.processing import work


async def check_state(message: Message, bot: Bot, state: FSMContext):
    data = await state.get_data()
    files_info = data.get('files_info')
    print(data)


async def add_document_state(message: Message, bot: Bot, state: FSMContext):
    data = await state.get_data()  # Получение данных из состояния
    files_info = data.get('files_info', [])
    file = await bot.get_file(message.document.file_id)
    file_path = file.file_path
    file_info = {
        'file_id': message.document.file_id,
        'file_name': message.document.file_name,
        'file_size': message.document.file_size,
        'file_path': file_path
    }
    files_info.append(file_info)  # Добавление информации о файле в список файлов
    await state.update_data(files_info=files_info)  # Обновление данных в состоянии
    # await state.set_state(StepsDocuments.CHECK_DOCUMENT)
    # print(data)
    # print(files_info)
    # await state.update_data(files_info=files_info)  # Обновление данных в состоянии
    # await state.set_state(StepsDocuments.CHECK_DOCUMENT)
    # if len(data) == 2:
    #     for i in files_info:
    #         await download(i["file_path"], i["file_name"], bot)


async def get_document(message: Message, bot: Bot, state: FSMContext):
    name_file = message.document.file_name
    file = await bot.get_file(message.document.file_id)
    file_path = file.file_path
    if name_file.endswith(".pdf"):
        file_pdf = {
            'file_id': message.document.file_id,
            'file_name': message.document.file_name,
            'file_size': message.document.file_size,
            'file_path': file_path
        }
        await state.update_data(file_pdf=file_pdf)
    elif name_file.endswith(".xlsx"):
        file_xlsx = {
            'file_id': message.document.file_id,
            'file_name': message.document.file_name,
            'file_size': message.document.file_size,
            'file_path': file_path
        }
        await state.update_data(file_xlsx=file_xlsx)
    else:
        await message.reply(f"Такие файлы я не обрабытываю {name_file}")
        return
    await state.set_state(StepsDocuments.CHECK_DOCUMENT)
    data = await state.get_data()
    print(data)
    if len(data) == 2:
        name = data["file_pdf"]["file_id"]
        await message.reply_document(name)


async def req_document(message: Message, state: FSMContext):
    await message.reply(f"{message.from_user.first_name} Присылай файлы!")
    await state.set_state(StepsDocuments.GET_DOCUMENT)
