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
    data = await state.get_data()  # Получение данных из состояния
    files_info = data.get('files_info', [])  # Получение информации о файлах или пустого списка, если информации еще нет
    file_info = {
        'file_id': message.document.file_id,
        'file_name': message.document.file_name,
        'file_size': message.document.file_size,
    }
    files_info.append(file_info)  # Добавление информации о файле в список файлов
    await state.update_data(files_info=files_info)  # Обновление данных в состоянии
    await state.set_state(StepsDocuments.CHECK_DOCUMENT)


async def check_document(message: Message, bot: Bot, state: FSMContext):
    resolved_extension = [".pdf", ".xlsx"]  # Список разрешонных
    recieved_extension = []  # Список полученых
    data = await state.get_data()
    files_info = data.get('files_info', [])
    match len(files_info):
        case 1:
            await message.answer("Получил Один файл. Ну что мне с ним делать. Нажми /help")
            await state.clear()  # Очищаем состояние
        case 2:
            await message.reply("Получил два файла!")
            files_size = 50000 < (files_info[0]["file_size"] + files_info[1]["file_size"])
            recieved_extension.append(os.path.splitext(files_info[0]["file_name"])[1])
            recieved_extension.append(os.path.splitext(files_info[1]["file_name"])[1])
            if Counter(resolved_extension) == Counter(recieved_extension) and files_size:
                await message.reply("Скачиваю файлы и проверяю.")
                await download(bot, state)  # Скачиваем файлы с телеграмма на сервер.
                await state.clear()  # Очищаем состояние
            else:
                await message.reply("Что то не то с расширениями файлов! Нажми /help")
                await state.clear()  # Очищаем состояние
        case _:
            await message.answer("Слушай что то перебор, почитай на /help что нужно делать!")
            await state.clear()  # Очищаем состояние







