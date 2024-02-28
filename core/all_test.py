import openpyxl
import re
from openpyxl.styles import PatternFill


def color_xlsx_cell(xlsx_file):
    wb = openpyxl.reader.excel.load_workbook(filename=xlsx_file)
    wb.active = 0
    sheet = wb.active

    for row in sheet.iter_rows():
        print(row[1].value)

if __name__ == '__main__':
    a, b, c = (5,)*3
    print(b)
    # color_xlsx_cell("C:\\robots\\RPA_check_documents\\test_doc\\1\\акт эф решение.xlsx")