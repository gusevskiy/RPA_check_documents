from environs import Env
from dataclasses import dataclass


@dataclass
class Bots:
    bot_token: str
    admin_id: int
    path_folder: str


@dataclass
class Settings:
    bots: Bots


# ф-я формирования объекта настроеК
def get_settings(path: str):
    env = Env()
    env.read_env(path)

    return Settings(
        bots=Bots(
            bot_token=env.str("TOKEN"),  # str
            admin_id=env.int("ADMIN_ID"),  # int
            path_folder=env.str("PATH_FOLDER")
        )
    )


# Считавем настройки из файла input
settings = get_settings('input')
# print(settings)  # test print
