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
            print(row)
            date = dict_match['date_document']
            number = dict_match['number_document']
            amount = dict_match['amount_invoice'].replace(' ', '').split(",")[0].split(",")[0]
            print(amount, row[4].value)
            all_true = number in str(row[3].value) and (int(amount) == row[4].value or int(amount) == row[5].value)
            all_false = number in str(row[3].value) and (int(amount) != row[4].value or int(amount) != row[5].value)
            d=1
            # if all_true:
            #     row[3].fill = PatternFill(fill_type='solid', start_color='00FF00')
            #     row[4].fill = PatternFill(fill_type='solid', start_color='00FF00')
            #     row[5].fill = PatternFill(fill_type='solid', start_color='00FF00')
            # elif number in str(row[3].value):
            #     row[3].fill = PatternFill(fill_type='solid', start_color='CD5C5C')
            #     row[4].fill = PatternFill(fill_type='solid', start_color='CD5C5C')
            #     row[5].fill = PatternFill(fill_type='solid', start_color='CD5C5C')
            
    wb.save('result.xlsx')
    


if __name__ == '__main__':
    list_matches_pdf_file = ['27.01.23\\nОплата (120 от 27.01.2023)\\n32 000,00', '31.01.23\\nПродажа (26 от 31.01.2023)\\n32 000,00', '28.02.23\\nПродажа (61 от 28.02.2023)\\n32 000,00', '01.03.23\\nОплата (283 от 01.03.2023)\\n32 000,00', '29.03.23\\nОплата (447 от 29.03.2023)\\n32 000,00', '31.03.23\\nПродажа (98 от 31.03.2023)\\n32 000,00', '30.04.23\\nПродажа (134 от 30.04.2023)\\n32 000,00', '10.05.23\\nОплата (627 от 10.05.2023)\\n32 000,00', '31.05.23\\nПродажа (171 от 31.05.2023)\\n32 000,00', '08.06.23\\nОплата (786 от 08.06.2023)\\n32 000,00', '30.06.23\\nПродажа (204 от 30.06.2023)\\n32 000,00', '11.07.23\\nОплата (971 от 11.07.2023)\\n32 000,00', '31.07.23\\nПродажа (243 от 31.07.2023)\\n32 000,00', '17.08.23\\nОплата (1130 от 17.08.2023)\\n32 000,00', '18.08.23\\nОплата (1136 от 18.08.2023)\\n32 000,00', '31.08.23\\nПродажа (277 от 31.08.2023)\\n32 000,00']
    xlsx_file = 'aiogram-bot\chat_files\акт эф решение.xlsx'
    
    color_xlsx_cell(list_matches_pdf_file, xlsx_file)