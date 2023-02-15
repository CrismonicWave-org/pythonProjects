import openpyxl

# Load the workbook
wb = openpyxl.load_workbook("testbook1.xlsx")

# Get a list of all worksheet names in the workbook
worksheet_names = wb.sheetnames
print("Number of worksheets=" + str(len(worksheet_names)))

# Print the worksheet names
print(worksheet_names)
