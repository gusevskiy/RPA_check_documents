import os
import re
import fitz
import openpyxl
import logging
import sys
from aiogram import Bot

from aiogram.types import Message, Document

from aiogram.fsm.context import FSMContext

from core.processing.read_xlsx import color_xlsx_cell
from openpyxl.styles import Font, Color, PatternFill

# xlsx_file = ''
# pdf_file = ''





def read_pdf_file(file_path) -> str:
    """
    Принимает ссылку на файл pdf 
    возвращает весь извлеченный текст в формате строки.
    """
    doc = fitz.open(file_path)
    all_text_from_pdf = []
    for page in doc:
        text = page.get_text()
        all_text_from_pdf.append(text)
    print(all_text_from_pdf)
    return str(all_text_from_pdf)


def check_verification_act(all_text_from_pdf, xlsx_file) -> str:
    """
    Проверяет названия документов, то что это акты сверки.
    Возвращает заголовки из этих документов: название, период, юр.л.
    """
    title_xlsx = ''
    title_pdf = ''
    wb = openpyxl.reader.excel.load_workbook(filename=xlsx_file)
    wb.active = 0
    sheet = wb.active
    if "акт сверки" in sheet['D1'].value.lower():
        title_xlsx = f"{sheet['D1'].value} {sheet['B2'].value} {sheet['B3'].value}"
        title_xlsx = title_xlsx.replace("И", " ")
    reg = r"(?P<title_pdf>Акт[\s]*сверки[\s\S]*период:[\s\S]*)Мы"
    if "акт сверки" in all_text_from_pdf[0:20].lower():
        title_pdf = ' '.join(re.findall(reg, all_text_from_pdf)).replace(r"\n", " ")
    return f"{title_pdf} \n \n {title_xlsx}"


def file_regex_search(all_text_from_pdf: str) -> list:
    """
    Принимает строку текста,
    возвращает список со всеми найденными совпадениями
    """
    reg = r"\d{2}\.\d{2}\.\d{2}[\s|\\n]*[А-яЁё]{0,7}[\s|\\n]*\(\d{0,4}[\s|\\n]*от[\s|\\n]\d{2}[\s|\\n]*\.\d{2}\.\d{4}\)[\s|\\n]*\d{0,4}[\s|\\n]*\d{3}\,\d{2}"
    list_matches_pdf_file = re.findall(reg, all_text_from_pdf)
    return list_matches_pdf_file


def search_matches_xlsx_file(list_matches_pdf_file, xlsx_file):
    """ Принимает список всех совпадений из pdf_file и ссылку на xlsx_file
        передает их в функцию color_xlsx_cell в файле read_xlsx
        результат формируется копия xlsx_file => result.xlsx
        со всеми пометками совпадений.
    """
    color_xlsx_cell(list_matches_pdf_file, xlsx_file)


async def work_main(file_pdf, file_xlsx):
    try:
        all_text_from_pdf = read_pdf_file(file_pdf)
        logging.info('Текст из pdf_file получен')
        result = check_verification_act(all_text_from_pdf, file_xlsx)
        logging.info('Отправлено два заголовка в чат')
        return result

        # list_matches_pdf_file = file_regex_search(all_text_from_pdf)
        # logging.info('совпадения из pdf_file получены')
        # search_matches_xlsx_file(list_matches_pdf_file, xlsx_file)
        # logging.info('Файл xlsx_file раскрашен')
    except Exception as e:
        print(e, 'Error1')


# if __name__ == '__main__':
#     logging.basicConfig(
#         level=logging.INFO,
#         handlers=[
#             logging.FileHandler(
#                 os.path.abspath('bot_log.log'), mode='w', encoding='UTF-8'
#             ),
#             logging.StreamHandler(stream=sys.stdout)
#         ],
#         format='%(asctime)s, %(levelname)s, %(funcName)s, '
#                '%(lineno)s, %(name)s, %(message)s'
#     )
#     work_main()
