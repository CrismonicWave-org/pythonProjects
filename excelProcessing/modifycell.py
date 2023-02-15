import openpyxl

# Load the workbook
wb = openpyxl.load_workbook("testbook1.xlsx")

# Select the sheet you want to modify
sheet = wb["Sheet1"]

# Define the cell you want to change
cell_to_change = "B20"

# Define the new value for the cell
new_value = 1

# Get the cell object and change its value
cell = sheet[cell_to_change]
tValue = int(cell.value)
tValue += new_value
cell.value = tValue

# Save the changes to the workbook
wb.save("testbook1.xlsx")

# Close the workbook
wb.close()
