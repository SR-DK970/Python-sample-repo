import openpyxl

"""path = "D:\DK-R\Monthly-Invoices.xlsx"
invoice_file = openpyxl.load_workbook(path)
sold_items = invoice_file["Sheet1"]

print(sold_items)

for product_row in range(2, sold_items.max_row + 2):
    print(product_row) """

import pandas

excel_data = pandas.read_excel('Monthly-Invoices.xlsx', sheet_name='Sheet1')
def read_excel():

    column1 = excel_data['Shirts'].tolist()
    column2 = excel_data['T-Shirts'].tolist()
    add = column1 + column2
    return add
    #for i in enumerate(column1):
        #print(i)
print(read_excel())

def update_excel():
    # Append the new data to the sheet
    excel_data.append(read_excel())
    # Save the workbook
    excel_data.save(read_excel())


print(update_excel())




# print whole sheet data
#print(excel_data)
#print(excel_data.columns)




