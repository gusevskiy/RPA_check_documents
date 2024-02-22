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
    print(data)


async def add_document_state(message, bot, state):
    data = await state.get_data()
    files_info = data.get('files_info', [])
    file = await bot.get_file(message.document.file_id)
    file_path = file.file_path
    file_info = {
        'file_id': message.document.file_id,
        'file_name': message.document.file_name,
        'file_size': message.document.file_size,
        'file_path': file_path
    }
    files_info.append(file_info)
    await state.update_data(files_info=files_info)


async def get_document(message: Message, bot: Bot, state: FSMContext):
    id_file = message.document.file_id
    name_file = message.document.file_name
    size_file = message.document.file_size
    path_file = (await bot.get_file(id_file)).file_path
    if name_file.endswith(".pdf"):
        await add_document_state(message, bot, state)
    elif name_file.endswith(".xlsx"):
        await add_document_state(message, bot, state)
    else:
        await message.reply(f"Такие файлы я не обрабытываю {name_file}")
        return
    await state.set_state(StepsDocuments.CHECK_DOCUMENT)
    data = await state.get_data()
    if len(data["files_info"]) == 2:
        for i in data["files_info"]:
            key_path = i["file_path"]
            key_name = i["file_name"]
            await download(key_path, key_name, bot)
        # await message.reply_document(name)


async def req_document(message: Message, state: FSMContext):
    await message.reply(f"{message.from_user.first_name} Присылай файлы!")
    await state.set_state(StepsDocuments.GET_DOCUMENT)
