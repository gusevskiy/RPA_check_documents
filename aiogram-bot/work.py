import os
import re
import fitz
import fnmatch
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


def read_pdf_file(file_path):
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


def file_regex_search(all_text_from_pdf):
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

    


def main():
    pathfile=f"{os.path.dirname(os.path.abspath(__file__))}\\chat_files"
    check_files(pathfile)
    all_text_from_pdf = ''
    if 'pdf_file' in globals():
        all_text_from_pdf = read_pdf_file(pdf_file)
    list_matches_pdf_file = file_regex_search(all_text_from_pdf)
    search_matches_xlsx_file(list_matches_pdf_file, xlsx_file)


if __name__ == '__main__':
    main()