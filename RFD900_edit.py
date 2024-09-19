import openpyxl as xl


def RFD_process(input_file_path, output_file_path):
    wb = xl.load_workbook(input_file_path)
    ws = wb.active  # Assuming we want the active sheet
    print("Working on: " + input_file_path)
    # Loop through column B starting from row 2

    # Save the workbook with the updated values to a different file path
    wb.save(output_file_path)
    print(f"\n Workbook saved to '{output_file_path}' successfully.")
