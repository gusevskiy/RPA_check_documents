import asyncio
import os
import logging
from aiogram import Bot, Dispatcher, F, types, Router
from aiogram.types import ContentType
from aiogram.filters.command import Command
from dotenv import load_dotenv


load_dotenv()
TOKEN = os.getenv('TOKEN')
# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token=TOKEN)
# Диспетчер
dp = Dispatcher()


@dp.message(F.document)
async def save_file(message: types.Message, bot: Bot):
    name_file = message.document.file_name
    if name_file.endswith(".pdf") | name_file.endswith(".xlsx"):
        file_id = message.document.file_id
        file = await bot.get_file(file_id)
        file_path = file.file_path
        name_file = message.document.file_name
        # print(file_id)
        # print(file)
        # print(file_path)
        destination=f"C:\\robots\\RPA_telegram\\chat_files\\{name_file}"
        await bot.download_file(file_path, destination=destination)
    else:
        await message.answer(text='Мне такое расширение файлов не нужно!')

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Кнопка 1")],
        [types.KeyboardButton(text="Кнопка 2")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    await message.answer(
        f"Вы девушка должны загрузить мне два файла " "\n" # noqa: F541
        f"один с разширением PDF, тот из которого ищем, " "\n"  # noqa: F541
        f"второй с расширением XLSX, в котором ищем!",  # noqa: F541
        reply_markup=keyboard
    )


@dp.message()
async def send_message(message: types.Message):
    await message.answer(
        text='Не надо мне писать, \n'
             'я сам тебе напишу если захочу!'
    )




# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())




# @dp.message()
# async def save_file(message: types.Message, bot: Bot):
#     file_id = message.document.file_id
#     name_file = message.document.file_name
#     file = bot.get_file(file_id)
#     file_path = file.file_path
#     downloaded_file = bot.download_file(file)
#     print("Это print", downloaded_file)
#     document = message.document
#     # await bot.download(document)
#     await bot.download_file(file_path, name_file)
#     # destination=f"C:\\robots\\RPA_telegram\\chat_files\\{name_file}.pdf"
#     # print(name_file, destination)
#     # await bot.download(document, destination=destination)