from __future__ import print_function
import clr
# https://learn.microsoft.com/en-us/dotnet/api/microsoft.office.interop.excel?view=excel-pia
clr.AddReference("Microsoft.Office.Interop.Excel")

# import Application
import Microsoft.Office.Interop.Excel as Excel

# Create excel object
excel = Excel.ApplicationClass()

# Make the excel application visible
excel.Visible = True
excel.DisplayAlerts = False

# add workbook
def createNewWorkbook(filepath, format):
    if format == "xlsx":
        wbFormat = Excel.XlFileFormat.xlWorkbookDefault
    elif format == "csv":
        wbFormat = Excel.XlFileFormat.xlCSV
    workbook = excel.Workbooks.Add()
    workbook.SaveAs(Filename = filepath, FileFormat = wbFormat, AccessMode = Excel.XlSaveAsAccessMode.xlNoChange)
    return workbook

def readWorkbook(workbookPath):
    workbook = excel.Workbooks.Open(workbookPath)
    return workbook

def readWorksheet(workbook, worksheetName = 1):
    worksheet = workbook.Worksheets[worksheetName]
    worksheetRange = worksheet.UsedRange
    rowCount = worksheetRange.Rows.Count
    colCount = worksheetRange.Columns.Count
    # print(rowCount, colCount)
    return worksheet

def getHeaderIndex(worksheet, columnName):
    worksheetRange = worksheet.UsedRange
    for colIndex in range(1, worksheetRange.Columns.Count):
        if worksheetRange.Cells[1, colIndex].Value2 == columnName:
            return colIndex

def printWorksheet(worksheet):
    worksheetRange = worksheet.UsedRange
    rowCount = worksheetRange.Rows.Count
    colCount = worksheetRange.Columns.Count
    for row in range(1, rowCount+1):
        for col in range(1, colCount+1):
            print(worksheetRange.Cells[row, col].Value2, end="\t")
        print("\n")


def insertRow(worksheet, rowList):
    worksheetRange = worksheet.UsedRange
    rowCount = worksheetRange.Rows.Count
    colCount = worksheetRange.Columns.Count
    for col in range(1, len(rowList)+1):
        if worksheetRange.Cells[1, 1].Value2 == "":
            worksheetRange.Cells[1, col] = rowList[col-1]
        else:
            worksheetRange.Cells[rowCount+1, col] = rowList[col-1]

def exitWorkbook(workbook):
    workbook.Save()
    workbook.Close()
    excel.Quit()

def createTableFromRange(worksheet, tableName, tableStyleName = "TableStyleMedium2"):
    worksheet.ListObjects.Add(SourceType = Excel.XlListObjectSourceType.xlSrcRange, Source = worksheet.UsedRange, XlListObjectHasHeaders = Excel.XlYesNoGuess.xlYes).Name = tableName
    worksheet.ListObjects[tableName].TableStyle = tableStyleName

try:
    # createNewWorkbook(r"D:\AnsysScripting\003 Excel from IronPython\ansys", "xlsx")
    wb = readWorkbook(r"D:\AnsysScripting\003 Excel from IronPython\ansys.xlsx")
    ws = readWorksheet(wb)
    # insertRow(ws, ['1', 'aa'])
    # printWorksheet(ws)
    # createTableFromRange(ws, "Table1")
    # print(ws.ListObjects["Table1"].ListRows)
    exitWorkbook(wb)
except:
    exitWorkbook(wb)
