import os
from import_data import base_path, list_excel_files
from Ptero_edit import Ptero_process
from RFD900_edit import RFD_process

print("NEBP Pterodactyl Data Editor \n")


def process_workbook(selected_file_path, output_file_path):
    # Stub function to process the workbook
    print(f"Processing file: {selected_file_path}")
    print(f"Saving to: {output_file_path}")
    # Add actual processing logic here


def main():
    while True:
        # List and select the Excel file from the folder
        selected_file_path, file_prefix = list_excel_files(base_path)

        if selected_file_path:
            print(f"\nSelected file: {selected_file_path}")

            # Extract folder names
            base_folder = os.path.basename(os.path.dirname(os.path.dirname(selected_file_path)))
            sub_folder = os.path.basename(os.path.dirname(selected_file_path))

            # Define the output file path dynamically
            output_dir = os.path.join(
                base_path,  # Start from the base path
                base_folder,  # Include the base folder
                sub_folder,  # Include the sub-folder
                'Modified'  # The directory where modified files will be saved
            )

            output_file_path = os.path.join(
                output_dir,
                os.path.basename(selected_file_path)  # Maintain the original file name
            )

            # Ensure the output directory exists
            os.makedirs(output_dir, exist_ok=True)

            # Process the selected file based on its prefix
            if file_prefix == "PTER":
                print(f"Processing with Ptero function.")
                Ptero_process(selected_file_path, output_file_path)
            elif file_prefix == "RFD900":
                print(f"Processing with RFD900 function.")
                RFD_process(selected_file_path, output_file_path)
            else:
                print("Unknown file prefix. Exiting.")
                exit(0)

            break  # Exit the loop after processing the file
        else:
            print("No files selected. Have a good day.")
            exit(0)


if __name__ == "__main__":
    main()
