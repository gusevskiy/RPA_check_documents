import asyncio
import os
import logging
from aiogram import Bot, Dispatcher, F, types
from aiogram.filters.command import Command
from aiogram.types import FSInputFile
from dotenv import load_dotenv
from work import main1


load_dotenv()


TELEGRAM_TOKEN = os.getenv('TOKEN')
TELEGRAM_CHAT_ID = os.getenv('CHAT_ID')
pathfile = f"{os.path.dirname(os.path.abspath(__file__))}\\chat_files"

# Объект бота
bot = Bot(token=TELEGRAM_TOKEN)
# Диспетчер
dp = Dispatcher()


@dp.message(F.document)
async def save_file(message: types.Message, bot: Bot):
    """ 
    Получены файлы в чат, если pdf или xlsx 
    сохранит их в папку chat_files.
    """
    name_file = message.document.file_name
    if name_file.endswith(".pdf") | name_file.endswith(".xlsx"):
        file_id = message.document.file_id
        file = await bot.get_file(file_id)
        file_path = file.file_path
        name_file = message.document.file_name
        # нужно создать папку chat_files если ее нет
        if not os.path.exists(pathfile):
            os.makedirs(pathfile)
        destination = f"{pathfile}\\{name_file}"
        await bot.download_file(file_path, destination=destination)
    else:
        await message.answer(text='Мне такое расширение файлов не нужно!')


def delete_file(pathfile):
    """
    Удаляет все файлы из папки.
    """
    # if os.path.exists(pathfile):
    for filename in os.listdir(pathfile):
        os.remove(pathfile+"\\"+filename)


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    """ 
    Создание кнопок, а текст на кнопках это команды
    """
    kb = [
        [types.KeyboardButton(text="проверить")],
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    await message.answer(
        f"Вы товарищ должны загрузить мне два файла " "\n"  # noqa: F541
        f"один с разширением PDF, тот из которого ищем, " "\n"  # noqa: F541
        f"второй с расширением XLSX, в котором ищем!",  # noqa: F541
        reply_markup=keyboard
    )


@dp.message()
async def send_message(message: types.Message):
    """
    Реагирует на текст в чате.
    """
    chat_id = message.chat.id
    adm = TELEGRAM_CHAT_ID
    file_send = pathfile+'\\'+''.join([name for name in os.listdir(pathfile) if name.endswith('.xlsx')])
    # file_send = 'C:\\DEV_python\\RPA_check_documents\\test.xlsx'
    if str(message.chat.id) not in adm:
        await bot.send_message(message.chat.id, 'Мой хозяин вас не знает, '
                                                'мне запрещено с '
                                                'вами разговаривать!!!')
    elif message.text == 'проверить':
        main1()
        # await message.reply_document(open("test.xlsx", 'rb'))
        await bot.send_document(chat_id, FSInputFile(file_send))
        delete_file(pathfile)
        
    else:
        await message.answer(
            text='Не надо мне писать, \n'
                'я сам тебе напишу если захочу! \n'
                'Два файла пришли мне на проверку и все!'
        )


async def main() -> None:
    logging.basicConfig(level=logging.INFO)
    
    # Запускаем бота и пропускаем все накопленные входящие
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
    # pathfile=f"{os.path.dirname(os.path.abspath(__file__))}\\chat_files"
    # print(pathfile+'\\'+''.join([name for name in os.listdir(pathfile) if name.endswith('.xlsx')]))