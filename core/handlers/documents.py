from aiogram import Bot
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from core.utils.statedocuments import StepsDocuments
from core.settings import settings


# async def download(message: Message, bot: Bot, state: FSMContext):
#     doc = await bot.get_file(message.document.file_id)
#     name_doc = message.document.file_name
#     # file_path = doc.file_path
#     await bot.download_file(
#         doc.file_path, f"{settings.bots.path_folder}\\{name_doc}"
#         # doc.file_path, destination=f"{pathfile}\\{name_doc}"
#     )
#     await state.set_state(StepsDocuments.GET_DOCUMENT)

# form
async def req_document(message: Message, state: FSMContext):
    await message.reply(f"{message.from_user.first_name} Присылай файлы!")
    await state.set_state(StepsDocuments.GET_DOCUMENT)


async def get_document(message: Message, state: FSMContext):
    data = await state.get_data()  # Получение данных из состояния
    files_info = data.get('files_info', [])  # Получение информации о файлах или пустого списка, если информации еще нет
    # Получение информации о полученном файле
    file_info = {
        'file_id': message.document.file_id,
        'file_name': message.document.file_name,
        'file_size': message.document.file_size
    }
    files_info.append(file_info)  # Добавление информации о файле в список файлов
    # print(files_info)
    # print(data)
    await state.update_data(files_info=files_info)  # Обновление данных в состоянии
    if files_info == 2:
        ...
    await state.set_state(StepsDocuments.CHECK_DOCUMENT)


async def check_document(message: Message, state: FSMContext):
    await message.answer("HI")
    data = await state.get_data()
    print(data)






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
