import os
from collections import Counter
from aiogram import Bot
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from core.utils.statedocuments import StepsDocuments
from core.utils.downloads import download
from core.processing import work


async def get_document1(message: Message, bot: Bot, state: FSMContext):
    data = await state.get_data()  # Получение данных из состояния
    files_info = data.get('files_info', [])  # Получение информации о файлах или пустого списка, если информации еще нет
    file = await bot.get_file(message.document.file_id)
    file_path = file.file_path
    file_info = {
        'file_id': message.document.file_id,
        'file_path': file_path,
        'file_name': message.document.file_name,
        'file_size': message.document.file_size,
        # 'file_path': file_path
    }
    files_info.append(file_info)  # Добавление информации о файле в список файлов
    await state.update_data(files_info=files_info)  # Обновление данных в состоянии
    if len(files_info):
        for i in files_info:
            await download(i["file_path"], i["file_name"], bot)



async def req_document(message: Message, state: FSMContext):
    await message.reply(f"{message.from_user.first_name} Присылай файлы!")
    await state.set_state(StepsDocuments.GET_DOCUMENT)


async def get_document2(message: Message, bot: Bot, state: FSMContext):
    file_name = message.document.file_name
    file_id = message.document.file_id
    file_path = (await bot.get_file(file_id)).file_path
    if file_name.endswith(".pdf"):
        await download(file_path, file_name, bot)
    elif file_name.endswith(".xlsx"):
        await download(file_path, file_name, bot)
    else:
        await message.reply(f"Такие файлы я не обрабытываю {file_name}")
        return
    # if len(data) == 2:
    #     await download(bot, state)







