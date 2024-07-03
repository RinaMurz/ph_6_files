from xlrd import open_workbook

workbook = open_workbook("tmp/file_example_XLS_10.xls")

print(workbook.nsheets) # печать количества страниц

print(workbook.sheet_names()) # печать названия страницы

sheet = workbook.sheet_by_index(0) # вызвать лист по индексу

print(sheet.nrows)
print(sheet.ncols)

print(sheet.cell_value(rowx=9, colx=3))

#другой вариант

#print(f'Количество столбцов {sheet.ncols}') # печать с листа количество столбцов

#print(f'Количество строк {sheet.nrows}') # печать с листа количество строк

#print(f'Ячейка 9:1 = {sheet.cell_value(rowx=9, colx=1)}') # печать содержимого ячейки

for rx in range(sheet.nrows): # печать содержимого всех ячеек
    print(sheet.row(rx))