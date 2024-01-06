from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault


async def set_commands(bot: Bot):
    commands = [
        BotCommand(
            command='start',
            description='start of work'
        ),
        BotCommand(
            command='help',
            description='help'
        ),
        BotCommand(
            command='cancel',
            description='cancel'
        ),
        BotCommand(
            command='inline',
            description='showing inline buttons'
        )
    ]

    await bot.set_my_commands(commands, BotCommandScopeDefault())
