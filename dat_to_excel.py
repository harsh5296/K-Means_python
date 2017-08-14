data = []
with open("data.txt") as f:
        for line in f:
                data.append([word for word in line.split(",") if word])
print data

import xlwt
wb = xlwt.Workbook()
sheet = wb.add_sheet("New Sheet")
for row_index in range(len(data)):
	for col_index in range(len(data[row_index])):
		sheet.write(row_index, col_index, data[row_index][col_index])

wb.save("newSheet.xls")
