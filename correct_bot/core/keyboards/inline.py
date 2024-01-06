from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from core.utils.callbackdata import MacInfo


# First variant add inline keyboard
select_macbook = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
            text="Macbook Air 13* M1 2020",
            callback_data="apple_air_13_m1_2020"
            )
        ],
        [
            InlineKeyboardButton(
            text="Macbook Pro 14* M1 Pro 2021",
            callback_data="apple_pro_14_m1_2021"
            )
        ],
        [
            InlineKeyboardButton(
            text="Apple Macbook Pro 16* 2019",
            callback_data="apple_pro_16_i7_2019"
            )
        ],
        [
            InlineKeyboardButton(
            text="Link",
            url="https://nztcoder.com"
            )
        ],
        [
            InlineKeyboardButton(
            text="Profile",
            url="tg://user?id=452054525"
            )
        ],
    ]
)


# Еще один способ формирования инлайн кнопок
def get_inline_keyboard():
    keyboard_builder = InlineKeyboardBuilder()
    # # Вариант с парсингом строки данных о товара
    # keyboard_builder.button(text="Macbook Air 13* M1 2020", callback_data="apple_air_13_m1_2020")
    # keyboard_builder.button(text="Macbook Pro 14* M1 Pro 2021", callback_data="apple_pro_14_m1_2021")
    # keyboard_builder.button(text="Apple Macbook Pro 16* 2019", callback_data="apple_pro_16_i7_2019")
    # Варант с классом атрибутов callbackdata
    keyboard_builder.button(text="Macbook Air 13* M1 2020", callback_data=MacInfo(model='air', size=13, chip='m1', year=2020))
    keyboard_builder.button(text="Macbook Air 13* M1 2020", callback_data=MacInfo(model='pro', size=14, chip='m1', year=2021))
    keyboard_builder.button(text="Macbook Air 13* M1 2020", callback_data=MacInfo(model='pro', size=16, chip='i7', year=2019))
    keyboard_builder.button(text="Link", url="https://nztcoder.com")
    keyboard_builder.button(text="Profile", url="tg://user?id=452054525")

    keyboard_builder.adjust(3)
    return keyboard_builder.as_markup()


