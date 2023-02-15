import openpyxl

# Load the workbook
wb = openpyxl.load_workbook("testbook1.xlsx")

# Select the sheet you want to search
sheet = wb["Sheet1"]

# Define the text you want to search for
search_text = "Ken Was Here"

# Loop through each row in the sheet
for row in sheet.iter_rows():
    for cell in row:
        # Check if the cell value matches the search text
        if cell.value == search_text:
            print("Found match in cell ", cell.coordinate + " cellvalue=" + str(cell.value))

# Close the workbook
wb.close()
