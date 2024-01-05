import asyncio
import os
import logging
import fnmatch
from aiogram import Bot, Dispatcher, F, types
from aiogram.filters.command import Command
from aiogram.types import FSInputFile, InlineKeyboardButton, InlineKeyboardMarkup
from dotenv import load_dotenv
from work import work_main, check_verification_act

load_dotenv()

TELEGRAM_TOKEN = os.getenv('TOKEN')
TELEGRAM_CHAT_ID = os.getenv('CHAT_ID')
pathfile = f"{os.path.dirname(os.path.abspath(__file__))}\\chat_files"

# Объект бота
bot = Bot(token=TELEGRAM_TOKEN)
# Диспетчер
dp = Dispatcher()


# Создаем объекты инлайн-кнопок
button_1 = InlineKeyboardButton(
    text='Проверить',
    callback_data='big_button_1_pressed'
)
button_2 = InlineKeyboardButton(
    text='Отклонить или загрузить новые',
    callback_data='big_button_2_pressed'
)

# Создаем объект инлайн-клавиатуры
keyboard = InlineKeyboardMarkup(
    inline_keyboard=[[button_1], [button_2]]
)


def create_path_files(pathfile):
    """
    Функция принимает путь к папке с сохраненными файлами
    из телеграмм.
    Проверяет что файл '*.pdf' = 1 и '*.xlsx' = 1
    создает две глобальные переменные на эти два файла
    """
    if len(
        fnmatch.filter(os.listdir(pathfile), '*.pdf')
    ) == 1 and len(
        fnmatch.filter(os.listdir(pathfile), '*.xlsx')
    ) == 1:
        global pdf_file
        global xlsx_file
        for i in os.listdir(pathfile):
            if i.endswith('.pdf'):
                pdf_file = f'{pathfile}\\{i}'
            if i.endswith('.xlsx'):
                xlsx_file = f'{pathfile}\\{i}'
        return True
    else:
        return False


@dp.message(F.document)
async def save_file(message: types.Message, bot: Bot):
    """ 
    Получены файлы в чат, если pdf или xlsx 
    сохранит их в папку chat_files.
    """
    name_file = message.document.file_name
    # Минимальная проверка на этапе загрузки, тк на стадии загрузки
    # не прочитав файлы сделать что-то большее наверно нельзя
    if name_file.endswith(".pdf") | name_file.endswith(".xlsx"):
        file_id = message.document.file_id
        file = await bot.get_file(file_id)
        file_path = file.file_path
        name_file = message.document.file_name
        # нужно создать папку chat_files если ее нет
        if not os.path.exists(pathfile):
            os.makedirs(pathfile)
        destination = f"{pathfile}\\{name_file}"
        # Сохраняет файлы в папку
        await bot.download_file(file_path, destination=destination)
        if create_path_files(pathfile):
            # Получаем заголовки из файлов для отправки их в чат для проверки.
            text_title = str(work_main(pdf_file, xlsx_file))
            # Отправляем заголовки в чат
            # тк ф-я срабатывает на каждый файл то первый N one пропускаем
            if text_title != 'None':
                await message.answer(text_title, reply_markup=keyboard)
        else:
            await message.answer(text='Нужно отправить два акта сверки pdf и xlsx!')
    else:
        await message.answer(text='Мне такое расширение файлов не нужно!')


def delete_file(pathfile):
    """
    Удаляет все файлы из папки.
    """
    # if os.path.exists(pathfile):
    for filename in os.listdir(pathfile):
        os.remove(pathfile + "\\" + filename)


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
        f"один с расширением PDF, тот из которого ищем, " "\n"  # noqa: F541
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
    file_send = pathfile + '\\' + ''.join(
        [name for name in os.listdir(pathfile) if name.endswith('.xlsx')])
    if str(message.chat.id) not in adm:
        await bot.send_message(message.chat.id, 'Мой хозяин вас не знает, '
                                                'мне запрещено с '
                                                'вами разговаривать!!!')
    elif message.text == 'проверить':
        work_main()
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
    # asyncio.run(main())
    # if create_path_files(pathfile):
    #     print('yes')
    # print('no')