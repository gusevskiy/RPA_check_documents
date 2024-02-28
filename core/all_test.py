import openpyxl
import re
import fitz
from openpyxl.styles import PatternFill


pdf_path = "C:\\robots\\RPA_check_documents\\test_doc\\1\\Акт_сверки_взаиморасчетов_№_16_от_12_октября_2023 г_1.pdf"
doc = fitz.open(pdf_path)

# Выберем страницу для анализа
page = doc[0]  # Предполагаем, что таблица находится на первой странице

# Получаем список всех блоков текста на странице (включая их координаты)
blocks = page.get_text("blocks")

# Каждый блок представляет собой кортеж (x0, y0, x1, y1, text, block_type, block_number)
# где (x0, y0) - координаты левого верхнего угла, (x1, y1) - координаты правого нижнего угла блока
for block in blocks:
    x0, y0, x1, y1, text, block_type, block_number = block
    if bool(re.search(r'\d{2}.\d{2}.\d{2,4}', text)):
        print(text)

# Закрываем документ после использования
doc.close()