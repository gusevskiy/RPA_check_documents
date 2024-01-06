from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    KeyboardButtonPollType
)
from aiogram.utils.keyboard import ReplyKeyboardBuilder


reply_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="row 1, column 1"),
            KeyboardButton(text="row 1, column 2"),
            KeyboardButton(text="row 1, column 3"),
        ],
        [
            KeyboardButton(text="row 2, column 1"),
            KeyboardButton(text="row 2, column 2"),
            KeyboardButton(text="row 2, column 3"),
            KeyboardButton(text="row 2, column 4"),
        ],
        [
            KeyboardButton(text="row 3, column 1"),
            KeyboardButton(text="row 3, column 2"),
        ]
    ],
    resize_keyboard=True,  # compact keyboard
    one_time_keyboard=True,  # hide keyboard
    input_field_placeholder='choose a button ↓',  # заполнитель текстового поля
    selective=True  # keyboard for the user only, use in groups
)

loc_tel_poll_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Send geolocation', request_location=True)],
        [KeyboardButton(text='Send contact', request_contact=True)],
        [KeyboardButton(
            # про Викторина и опросы отдельно нужно почитать
            text='Send quiz', request_poll=KeyboardButtonPollType()
        )]
    ],
    resize_keyboard=True,  # compact keyboard
    one_time_keyboard=False,  # hide keyboard
    input_field_placeholder='отправь локациюб номер телефона или создай викторину.опрос'  # заполнитель текстового поля
    # selective=True  # keyboard for the user only, use in groups
)


def get_reply_keyboard():
    keyword_builder = ReplyKeyboardBuilder()

    keyword_builder.button(text="botton 1")
    keyword_builder.button(text="botton 2")
    keyword_builder.button(text="botton 2")
    keyword_builder.button(text="Send location", request_location=True)
    keyword_builder.button(text="Send mine contact", request_contact=True)
    keyword_builder.button(text="Send quiz", request_poll=KeyboardButtonPollType())
    keyword_builder.adjust(3, 2, 1)
    return keyword_builder.as_markup(
        resize_keyboard=True,  # compact keyboard
        one_time_keyboard=False,  # hide keyboard
        input_field_placeholder='отправь локацию, номер телефона или создай викторину.опрос'  # заполнитель текстового поля
    )
