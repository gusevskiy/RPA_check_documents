from aiogram import Bot, Dispatcher
from aiogram.types import Message
import asyncio

token = '6513692439:AAFFgGmpXQfJzFsEUSiEP3FFK5QIZNqimO4'

async def start_bot(bot: Bot):
    await bot.send_message(452054525, text="Bot started")


async def stop_bot(bot: Bot):
    await bot.send_message(452054525, text="Bot stopped")


async def get_start(message: Message, bot: Bot):
    await message.answer(
        f"Привет {message.from_user.first_name}. Рад тебя видеть!"
    )


async def start():
    bot = Bot(token=token)
    dp = Dispatcher()
    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)

    dp.message.register(get_start)
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == '__main__':
    asyncio.run(start())
