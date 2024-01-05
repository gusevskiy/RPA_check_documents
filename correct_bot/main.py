from aiogram import Bot, Dispatcher
import asyncio

token = '6513692439:AAFFgGmpXQfJzFsEUSiEP3FFK5QIZNqimO4'





async def start():
    bot = Bot(token=token)
    dp = Dispatcher()
    try:
        await dp.start_polling()
    finally:
        await dp.stop_polling()


if __name__ == '__main__':
    asyncio.run(start())