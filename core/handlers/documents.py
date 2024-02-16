import os
from collections import Counter
from aiogram import Bot
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from core.utils.statedocuments import StepsDocuments
from core.settings import settings


async def download(message: Message, bot: Bot, stste: FSMContext):
    doc = await bot.get_file(message.document.file_id)
    name_doc = message.document.file_name
    # file_path = doc.file_path
    await bot.download_file(
        doc.file_path, f"{settings.bots.path_folder}\\{name_doc}"
        # doc.file_path, destination=f"{pathfile}\\{name_doc}"
    )

async def req_document(message: Message, state: FSMContext):
    await message.reply(f"{message.from_user.first_name} Присылай файлы!")
    await state.set_state(StepsDocuments.GET_DOCUMENT)


async def get_document(message: Message, bot: Bot, state: FSMContext):
    resolved_extension = [".pdf", ".xlsx"]
    recieved_extension = []
    data = await state.get_data()  # Получение данных из состояния
    files_info = data.get('files_info', [])  # Получение информации о файлах или пустого списка, если информации еще нет
    # Получение информации о полученном файле
    file_info = {
        'file_id': message.document.file_id,
        'file_name': message.document.file_name,
        'file_size': message.document.file_size,
    }
    files_info.append(file_info)  # Добавление информации о файле в список файлов
    await state.update_data(files_info=files_info)  # Обновление данных в состоянии
    print(len(files_info))
    print(files_info)
    files_size = files_info[0]["file_size"]
    # if len(files_info) == 2:
    #     await message.reply("Получил два файла!")
    #     recieved_extension.append(os.path.splitext(files_info[0]["file_name"])[1])
    #     recieved_extension.append(os.path.splitext(files_info[1]["file_name"])[1])
    #     if Counter(resolved_extension) == Counter(recieved_extension):
    #         await message.reply("Скачиваю файлы и проверяю.")
    #         await download(message, bot, state)
    #         # print(data)
    #     else:
    #         await message.reply("Что то не то с расширениями файлов! Нажми /help")


    # await state.set_state(StepsDocuments.CHECK_DOCUMENT)


# async def check_document(message: Message, state: FSMContext):
#     await message.answer("HI")
#     data = await state.get_data()
#     print(data)






# async def finish_upload(message: Message, state: FSMContext):
#     user_data = await state.get_data()
#     print(user_data)
#     files_count = user_data.get('files_count', 0)
#     await message.reply(f"Получено файлов: {files_count}. Обработка...")
#     await state.clear()
#
#
# async def handle_file(message: Message, state: FSMContext):
#     # Получаем текущее значение счетчика файлов
#     data = await state.get_data()
#     files = message.document
#     await state.update_data(key=files.file_id)
#
#     # files_count = data.get('files_count', 0) + 1
#     # Обновляем счетчик файлов в данных состояния
#     print(data)