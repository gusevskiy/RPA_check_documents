from aiogram import Bot
from aiogram.types import Message


async def get_start(message: Message, bot: Bot):
    await message.answer(
        f"<b>Привет {message.from_user.first_name}. Рад тебя видеть!</b>"
    )
    await message.answer(
        f"посмотреть инструкцию можно нажав кнопку Меню и выбрав /help"
    )


async def get_document(message: Message, bot: Bot):
    doc = await bot.get_file((message.document.file_id))
    filename = message.document.file_name
    await bot.download_file(
        doc.file_path, f"C:\\DEV_python\\RPA_check_documents\\docs\\{filename}"
    )
    await message.answer(
        f"Отлично, получил документ <{filename}>, сохраню себе и посмотрю что там."
    )