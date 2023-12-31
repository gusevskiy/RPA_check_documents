from aiogram import Bot, types
from aiogram import Dispatcher
import asyncio
from aiogram.filters.command import Command
import logging
from aiogram.types import FSInputFile, BufferedInputFile

API_TOKEN = '6513692439:AAFFgGmpXQfJzFsEUSiEP3FFK5QIZNqimO4'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

async def send_document(chat_id, file_path, caption):
    with open(file_path, 'rb') as document:
        dd = document.read()
        # Отправляем содержимое файла в чат
        await bot.send_document(chat_id, BufferedInputFile(dd, filename="file.pdf"))

@dp.message(Command("start"))
async def send_file_command(message: types.Message):
    # Путь к файлу на сервере
    file_path = 'C:\\DEV_python\\RPA_check_documents\\test.pdf'
    
    # Отправляем файл в чат
    await send_document(message.chat.id, file_path, caption='Это ваш файл!')

if __name__ == '__main__':
    # from aiogram import executor
    asyncio.run(dp.start_polling(bot))
