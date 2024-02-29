import openpyxl
import re
import fitz
from openpyxl.styles import PatternFill


pdf_path1 = "C:\\robots\\RPA_check_documents\\test_doc\\1\\Акт_сверки_взаиморасчетов_№_16_от_12_октября_2023 г_1.pdf"
pdf_path2 = "C:\\robots\\RPA_check_documents\\test_doc\\2\\Акт_сверки_взаиморасчетов_№_17_от_12_октября_2023_г_1.pdf"
pdf_path3 = "C:\\robots\\RPA_check_documents\\test_doc\\3\\акт_сверки_за_9_мес_2023_ИТ_Высота_Литвинова_с_ИП_Белов.pdf"
pdf_path4 = "C:\\robots\\RPA_check_documents\\test_doc\\4\\Эффективное решение ООО.pdf"

doc = fitz.open(pdf_path3)

all_text = []
for page in doc.pages():
    blocks = page.get_text('blocks')
    for block in blocks:
        x0, y0, x1, y1, text, block_type, block_number = block
        if text[0].isdigit():
            all_text.append(text)
print(str(all_text[0]))

# # Выберем страницу для анализа
# page = doc[0]  # Предполагаем, что таблица находится на первой странице

# # Получаем список всех блоков текста на странице (включая их координаты)
# blocks = page.get_text("blocks")

# # Каждый блок представляет собой кортеж (x0, y0, x1, y1, text, block_type, block_number)
# # где (x0, y0) - координаты левого верхнего угла, (x1, y1) - координаты правого нижнего угла блока
# for block in blocks:
#     # print(block)
#     x0, y0, x1, y1, text, block_type, block_number = block
#     # if text.startswitch(re.search(r'\d{2}\.\d{2}\.\d{2,4}')):
#     if text[0].isdigit():
#         print(text.split("\n"))

# Закрываем документ после использования
doc.close()
