import PyPDF2

file = open(r'''Enter PDF file location and name here''', 'rb')
reader = PyPDF2.PdfFileReader(file)


data = reader.getPage(2).extractText()
meter_number_loc = data.find('Meter Number: ')
print(data[meter_number_loc+14: meter_number_loc+22])


data = reader.getPage(2).extractText()
tax_loc = data.find('Total Taxes & Fees on Electric Charges')
print(data[tax_loc+50:tax_loc+55])

print(data.find('-1.41'))
