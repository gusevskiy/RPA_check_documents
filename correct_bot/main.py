from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
# from aiogram.types import Message, ContentType
from core.handlers.basic import get_start, get_photo, get_hello
from core.filters.iscontact import IsTrueContact
from core.handlers.contact import get_fake_contact, get_true_contact
import asyncio
import logging
from core.settings import settings
from core.utils.commands import set_commands
from core.handlers.basic import get_location
from core.handlers.basic import get_inline
from core.handlers.callback import select_macbook
from core.utils.callbackdata import MacInfo


async def start_bot(bot: Bot):
    await set_commands(bot)
    await bot.send_message(settings.bots.admin_id, text="Bot started")


async def stop_bot(bot: Bot):
    await bot.send_message(settings.bots.admin_id, text="Bot stopped")


async def start():
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s - [%(levelname)s] - %(name)s - "
                        "(%(filename)s).%(funcName)s(%(lineno)d) - %(message)s"
                        )
    # parse_mode = 'HTML' для выделения сообщений шрифтом.
    bot = Bot(token=settings.bots.bot_token, parse_mode='HTML')
    dp = Dispatcher()
    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)
    # dp.callback_query.register(select_macbook, F.data.startswith('apple_'))
    dp.callback_query.register(select_macbook, MacInfo.filter()) # можно установить фильтер на модель pro "MacInfo.filter(F.model == 'pro')
    dp.message.register(get_inline, Command(commands='inline'))
    dp.message.register(get_photo, F.photo)
    dp.message.register(get_location, F.location)
    dp.message.register(get_true_contact, F.contact, IsTrueContact())
    dp.message.register(get_fake_contact, F.contact)
    dp.message.register(get_hello, F.text == 'hello')
    dp.message.register(get_start, Command(commands=['start', 'run']))
    # dp.message.register(get_start, CommandStart())

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == '__main__':
    asyncio.run(start())
