from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, CommandStart
import asyncio
import logging
from core.settings import settings
from core.handlers.basic import get_start
from core.handlers import documents
from core.utils.statedocuments import StepsDocuments
from core.utils import downloads


async def start_bot(bot: Bot):
    await bot.send_message(
        settings.bots.admin_id, text="Bot started, press /start "
    )


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

    dp.message.register(documents.get_document, Command(commands="form"))
    dp.message.register(documents.answer, StepsDocuments.GET_DOCUMENT)


    dp.message.register(get_start, CommandStart())
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == '__main__':
    asyncio.run(start())
