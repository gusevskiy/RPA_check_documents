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

async def get_document(message: Message, state: FSMContext):
    await message.answer(
        f"{message.from_user.first_name},"
        f"Отправляй файлы, я проверю."
    )
    await state.set_state(StepsDocuments.GET_DOCUMENT)


async def answer(message: Message):
    await message.answer("Получил документ!")
