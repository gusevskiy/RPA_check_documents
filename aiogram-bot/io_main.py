import asyncio
import os
import logging
from aiogram import Bot, Dispatcher, F, types
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
pathfile=f"{os.path.dirname(os.path.abspath(__file__))}\\chat_files"

@dp.message(F.document)
async def save_file(message: types.Message, bot: Bot):
    name_file = message.document.file_name
    print(name_file)
    if name_file.endswith(".pdf") | name_file.endswith(".xlsx"):
        file_id = message.document.file_id
        file = await bot.get_file(file_id)
        file_path = file.file_path
        name_file = message.document.file_name
        # нужно создать папку chat_files если ее нет
        if not os.path.exists(pathfile):
            os.makedirs(pathfile)
        destination=f"{pathfile}\\{name_file}"
        await bot.download_file(file_path, destination=destination)
    else:
        await message.answer(text='Мне такое расширение файлов не нужно!')


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Кнопка 1")],
        [types.KeyboardButton(text="удалить файлы")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    await message.answer(
        f"Вы товарищ должны загрузить мне два файла " "\n" # noqa: F541
        f"один с разширением PDF, тот из которого ищем, " "\n"  # noqa: F541
        f"второй с расширением XLSX, в котором ищем!",  # noqa: F541
        reply_markup=keyboard
    )


@dp.message()
async def send_message(message: types.Message):
    adm = [452054525, ]
    if message.chat.id not in adm:
        await bot.send_message(message.chat.id, 'Мой хозяин вас не знает, '
                                                'мне запрещено с '
                                                'вами разговаривать!!!')
    elif message.text == 'удалить файлы':
        
        if os.path.exists(pathfile):
            for filename in os.listdir(pathfile):
                os.remove(pathfile+"\\"+filename)
    else:
        await message.answer(
            text='Не надо мне писать, \n'
                'я сам тебе напишу если захочу! \n'
                'Два файла пришли мне на проверку и все!'
        )


# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
