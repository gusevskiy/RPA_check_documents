from aiogram.types import Message


async def get_document(message: Message):
    await message.answer(
        f"{message.from_user.first_name},"
        f"начинаем проверять акты. Пришли два файла."
    )