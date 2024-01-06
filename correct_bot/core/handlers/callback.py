from aiogram import Bot
from aiogram.types import CallbackQuery
from core.utils.callbackdata import MacInfo


# async def select_macbook(call: CallbackQuery, bot: Bot):
#     model = call.data.split('_')[1]
#     size = call.data.split('_')[2]
#     chip = call.data.split('_')[3]
#     year = call.data.split('_')[4]
#     answer = f"{call.message.from_user.first_name}" \
#              f"choose Apple Macbook {model}" \
#              f"with a diagonal screen {size}, "\
#              f"processor {chip} {year} year."
#     await call.message.answer(answer)
#     await call.answer()

async def select_macbook(call: CallbackQuery, bot: Bot, callback_data: MacInfo):
    model = callback_data.model
    size = callback_data.size
    chip = callback_data.chip
    year = callback_data.year
    answer = f"{call.message.from_user.first_name}" \
             f"choose Apple Macbook {model}" \
             f"with a diagonal screen {size}, "\
             f"processor {chip} {year} year."
    await call.message.answer(answer)
    await call.answer()