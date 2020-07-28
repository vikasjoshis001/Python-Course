import pandas
file=pandas.ExcelFile("sales.xlsx")
# print(file.sheet_names)
sheet = file.parse("sales")
print(sheet)
