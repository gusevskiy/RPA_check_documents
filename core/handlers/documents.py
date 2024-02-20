import os
from collections import Counter
from aiogram import Bot
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from core.utils.statedocuments import StepsDocuments
from core.utils.downloads import download
from core.settings import settings





async def req_document(message: Message, state: FSMContext):
    await message.reply(f"{message.from_user.first_name} Присылай файлы!")
    await state.set_state(StepsDocuments.GET_DOCUMENT)


async def get_document(message: Message, state: FSMContext):
    # data = await state.get_data()  # Получение данных из состояния
    # files_info = data.get('files_info', {})
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
    await state.set_state(StepsDocuments.CHECK_DOCUMENT)
    # print(data)

async def open_stste(message: Message, state: FSMContext):
    data = await state.get_data()
    print(data)







