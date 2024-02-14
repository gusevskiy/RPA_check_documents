from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext


class StepsDocuments(StatesGroup):
    GET_DOCUMENT = State()
    CHECK_DOCUMENT = State()
    ALL_DOCUMENT = State()
