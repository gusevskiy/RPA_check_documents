from aiogram import Bot, types
from aiogram import Dispatcher
import asyncio
from aiogram.filters.command import CommandStart
import logging
from aiogram.types import FSInputFile, BufferedInputFile, InputFile

API_TOKEN = '6513692439:AAFFgGmpXQfJzFsEUSiEP3FFK5QIZNqimO4'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# async def send_document(chat_id, file_path, caption):
#     with open(file_path, 'rb') as document:
#         dd = document.read()
#         # Отправляем содержимое файла в чат
#         await bot.send_document(chat_id, BufferedInputFile(dd, filename="file.pdf"))

# @dp.message(Command("start"))
# async def send_file_command(message: types.Message):
#     # Путь к файлу на сервере
#     # file_path = 'C:\\DEV_python\\RPA_check_documents\\test.png'
#     with open(r'C:\\DEV_python\\RPA_check_documents\\test.png', 'rb') as document:
#         # file = BufferedInputFile(document.read(), 'any_filename')
#         await message.bot.send_document(message.from_user.id, "document.read()")

# @dp.message(Command("start"))
# async def send_file_command(message: types.Message):
#     file_path = 'C:\\DEV_python\\RPA_check_documents\\test.png'
#     file = open(file_path, 'rb')
#     await message.reply_document(file)


async def send_local_document(chat_id, file_path, caption):
    document = FSInputFile(file_path)
    await bot.send_document(chat_id, document)


@dp.message(CommandStart())
async def send_local_file_command(message: types.Message):
    # Путь к файлу на сервере
    file_path = 'C:\\DEV_python\\RPA_check_documents\\aiogram-bot\\chat_files\\акт эф решение.xlsx'

    # Отправляем локальный файл в чат
    await send_local_document(message.chat.id, file_path,
                              caption='Это ваш локальный файл!')


if __name__ == '__main__':
    # from aiogram import executor
    asyncio.run(dp.start_polling(bot))
