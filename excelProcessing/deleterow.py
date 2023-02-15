import openpyxl

# Load the workbook
wb = openpyxl.load_workbook("testbook1.xlsx")

# Select the sheet you want to modify
sheet = wb["Sheet1"]

# Define the row number you want to delete
row_to_delete = 17

# Delete the row
sheet.delete_rows(row_to_delete, 1)

# Save the changes to the workbook
wb.save("testbook1.xlsx")
