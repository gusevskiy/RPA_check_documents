import os
import re
import fitz
import fnmatch
import openpyxl
import logging
import sys
from read_xlsx import color_xlsx_cell
from openpyxl.styles import Font, Color, PatternFill

# xlsx_file = ''
# pdf_file = ''


def check_files(pathfile):
    """
    Функция принимает путь к папке с сохранеными файлами 
    из телеграмм.
    Проверяет что файл '*.pdf' = 1 и '*.xlsx' = 1
    создает две глобальные переменные на эти два файла
    """
    if len(
        fnmatch.filter(os.listdir(pathfile), '*.pdf')
    ) == 1 and len(
        fnmatch.filter(os.listdir(pathfile), '*.xlsx')
    ) == 1:
        global pdf_file
        global xlsx_file
        for i in os.listdir(pathfile):
            if i.endswith('.pdf'):
                pdf_file = f'{pathfile}\\{i}'
            if i.endswith('.xlsx'):
                xlsx_file = f'{pathfile}\\{i}'
        return True
    else:
        return False


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
    return str(all_text_from_pdf)


def check_verification_act(all_text_from_pdf, xlsx_file) -> str:
    """
    Проверяет названия документов, то что это акты сверки.
    Возвращает заголовки из этих документов: название, период, юр. л.
    """
    wb = openpyxl.reader.excel.load_workbook(filename=xlsx_file)
    wb.active = 0
    sheet = wb.active
    if "акт сверки" in sheet['D1'].value.lower():
        title_xlsx = f"{sheet['D1'].value} {sheet['B2'].value} {sheet['B3'].value}"
    reg = r"(?P<title_pdf>Акт[\s]*сверки[\s\S]*период:[\s\S]*)Мы"
    if "акт сверки" in all_text_from_pdf[0:20].lower():
        title_pdf = re.findall(reg, all_text_from_pdf) 
    
    return title_pdf, title_xlsx


def file_regex_search(all_text_from_pdf: str) -> list:
    """
    Принимает строку текста  
    Возвращает список со всеми найдеными совпадениями
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


def main1():
    try:
        pathfile=f"{os.path.dirname(os.path.abspath(__file__))}\\chat_files"
        check_files(pathfile)
        logging.info('Получино два файла pdf и xlsx')
        all_text_from_pdf = read_pdf_file(pdf_file)
        logging.info('Текст из pdf_file получен')
        list_matches_pdf_file = file_regex_search(all_text_from_pdf)
        logging.info('совпадения из pdf_file получены')
        search_matches_xlsx_file(list_matches_pdf_file, xlsx_file)
        logging.info('Файл xlsx_file раскрашен')
    except Exception as e:
        print(e, 'Error')


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
    main1()