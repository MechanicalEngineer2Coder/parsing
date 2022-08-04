#Access Excel file, modify and save report to PDF

import calendar
from datetime import date
import openpyxl
from openpyxl import Workbook, load_workbook
from copy import copy
from win32com.client import Dispatch
import os


todaysDate = date.today()
currentYear = todaysDate.year
currentMonth = todaysDate.month
if currentMonth==1:
    reportMonth = 12
    reportYear= currentYear - 1
else:
    reportMonth = currentMonth - 1
    reportYear = currentYear

#Reformat month to match Excels format
match reportMonth:
    case 1:
        reportMonth = "01"
    case 2:
        reportMonth = "02"
    case 3:
        reportMonth = "03"
    case 4:
        reportMonth = "04"
    case 5:
        reportMonth = "05"
    case 6:
        reportMonth = "06"
    case 7:
        reportMonth = "07"
    case 8:
        reportMonth = "08"
    case 9:
        reportMonth = "09"
    
#Open Excel log
file = '''Put Excel file location and name here'''
drawingWB = load_workbook(file)
drawingLogWS = drawingWB[str(currentYear)]

#print(reportMonth)

#Setup report
i = 5 #First row in log
startingRow = ""
cellValue = ""
firstDash = ""
secondDash = ""
finalRow = 0
while drawingLogWS["B" + str(i)].value is not None:
    cellValue = str(drawingLogWS["B"+str(i)].value)
    #Slice month out of date
    firstDash = cellValue.index('-')
    secondDash = cellValue.index('-', firstDash+1)
    if str(cellValue[firstDash+1:secondDash]) == str(reportMonth) and startingRow == "":
        startingRow = str(i)
    finalRow = i
    i+=1

#Shift uneeded cells right
moveRange = "B5:K" + str(int(startingRow)-1)
drawingLogWS.move_range(moveRange, cols=10)

#Move needed cells up
moveRange = "B" + startingRow + ":G" + str(finalRow)
moveRows = int(startingRow) - 5


drawingLogWS.move_range(moveRange, rows=-moveRows)

#Find new last row and setup print area
while drawingLogWS["B" + str(i)].value is not None:
    finalRow = i
    i+=1

printArea = "B2:G" + str(i-1)
drawingLogWS.print_area =  printArea
drawingWB.save(file)
drawingWB.close()

#Print
excel = Dispatch("Excel.Application")

sheets = excel.Workbooks.Open(file)
work_sheets = sheets.Worksheets[0]

#Build path for pdf
path = '''Put direct for PDF here'''
print(path)

#Print to PDF
work_sheets.ExportAsFixedFormat(0, path)
sheets.Close(True)
os.remove("C:/Users/robert/Desktop/Folders/Monthly Reports/DRAWING LOG 2.xlsx")
