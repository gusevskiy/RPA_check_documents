import os
from collections import Counter
from aiogram import Bot
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from core.utils.statedocuments import StepsDocuments
from core.utils.downloads import download
from core.settings import settings
from aiogram.types.input_file import FSInputFile





async def req_document(message: Message, state: FSMContext):
    await message.reply(f"{message.from_user.first_name} Присылай файлы!")
    await state.set_state(StepsDocuments.GET_DOCUMENT)


async def get_document(message: Message, bot: Bot, state: FSMContext):
    name_file = message.document.file_name
    if name_file.endswith(".pdf"):
        file_pdf = {
            'file_id': message.document.file_id,
            'file_name': message.document.file_name,
            'file_size': message.document.file_size,
        }
        await state.update_data(file_pdf=file_pdf)
    elif name_file.endswith(".xlsx"):
        file_xlsx = {
            'file_id': message.document.file_id,
            'file_name': message.document.file_name,
            'file_size': message.document.file_size,
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


async def open_stste(message: Message, state: FSMContext):
    data = await state.get_data()
    print(data)







