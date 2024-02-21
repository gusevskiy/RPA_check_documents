import logging
import sys
import os

from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, CommandStart
import asyncio
import logging
from aiogram.fsm.storage.memory import MemoryStorage
from core.settings import settings
from core.handlers import basic
from core.handlers import documents
from core.utils.statedocuments import StepsDocuments
from core.utils import downloads


async def start_bot(bot: Bot) -> None:
    """notyfi Started Bot"""
    await bot.send_message(
        settings.bots.admin_id, text="Bot started, press /start "
    )


async def stop_bot(bot: Bot) -> None:
    """notyfi Stopped Bot"""
    await bot.send_message(settings.bots.admin_id, text="Bot stopped")


async def start() -> None:
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s - [%(levelname)s] - %(name)s - "
                        "(%(filename)s).%(funcName)s(%(lineno)d) - %(message)s"
                        )
    storage = MemoryStorage()
    # parse_mode = 'HTML' для выделения сообщений шрифтом.
    bot = Bot(token=settings.bots.bot_token, parse_mode='HTML')
    dp = Dispatcher(storage=storage)
    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)

    dp.message.register(basic.get_start, CommandStart())
    dp.message.register(documents.req_document, Command(commands="form"))
    dp.message.register(basic.instruction, Command(commands="help"))
    # dp.message.register(documents.open_stste, Command(commands="check"))
    dp.message.register(documents.get_document1, F.document)
    dp.message.register(basic.response_to_test, F.text)

    try:
        # Запускаем бота и пропускаем все накопленные входящие
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == '__main__':
    logging.basicConfig(
        level=logging.INFO,
        handlers=[
            logging.FileHandler(
                os.path.abspath('bot_log.log'), mode='w', encoding='UTF-8'
            ),
            logging.StreamHandler(stream=sys.stdout)
        ],
        format='%(asctime)s, %(levelname)s, %(funcName)s, '
               '%(lineno)s, %(name)s, %(message)s'
    )
    asyncio.run(start())
