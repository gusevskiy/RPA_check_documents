import openpyxl


wb = openpyxl.reader.excel.load_workbook(filename='aiogram-bot\chat_files\акт эф решение.xlsx')
wb.active = 0
sheet = wb.active

print(sheet['D1'].value)
print(sheet['B2'].value)
print(sheet['B3'].value)