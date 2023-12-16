import openpyxl
import re
from openpyxl.styles import PatternFill




reg_groups = r"(?P<date_document>\d{2}\.\d{2}\.\d{2})[\s|\\n]*(?P<operation>[А-яЁё]{0,7})[\s|\\n]*\((?P<number_document>\d{0,5})[\s|\\n]*от[\s|\\n]\d{2}[\s|\\n]*\.\d{2}\.\d{4}\)[\s|\\n]*(?P<amount_invoice>\d{0,4}[\s|\\n]*\d{3}\,\d{2})"

def color_xlsx_cell(list_matches_pdf_file, xlsx_file):
    wb = openpyxl.reader.excel.load_workbook(filename=xlsx_file)
    wb.active = 0
    sheet = wb.active
    for match in list_matches_pdf_file:
        dict_match = re.search(reg_groups, match).groupdict()



        for row in sheet.iter_rows():
            if dict_match['date_document'] in str(row[2].value) and dict_match['number_document'] in [str(row[3].value) and dict_match['amount_invoce'] in str(row[5].value)]:
                row[3].fill = PatternFill(fill_type='solid', start_color='00FF00')
                row[5].fill = PatternFill(fill_type='solid', start_color='00FF00')

    wb.save('test.xlsx')