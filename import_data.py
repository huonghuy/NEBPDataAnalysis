import os
import sys

# Base directory where folders are located (you can modify this path)
base_path = "/Users/huyhuong/Documents/School/EEL/NEBP/Data_Analysis/"


def list_folders(folder_path):
    # List only directories inside the selected folder
    folders = [f for f in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, f))]

    if not folders:
        print("No folders found.")
        return None
    else:
        print("Available folders:")
        for idx, folder in enumerate(folders):
            print(f"{idx + 1}. {folder}")

    while True:
        # Prompt the user to select a folder or exit
        folder_index = input("\nSelect a folder by entering the number (or press 0 to go up one level): ")

        if folder_index == '0':
            return 'up'  # User chooses to go back to the parent directory

        try:
            folder_index = int(folder_index) - 1  # Convert to int and adjust for 0-based indexing

            if 0 <= folder_index < len(folders):
                selected_folder = folders[folder_index]
                return os.path.join(folder_path, selected_folder)
            else:
                print("Invalid selection. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def list_excel_files(folder_path):
    files = [f for f in os.listdir(folder_path) if f.endswith('.xlsx')]

    if not files:
        print("No Excel files found in this folder.")
        return None
    else:
        print("Available Excel files:")
        for idx, file in enumerate(files):
            file_name = os.path.splitext(file)[0]  # Remove the .xlsx extension
            parts = file_name.split('_')

            if len(parts) >= 2:
                # Assuming the second part (e.g., "CTUBR") contains both state and school
                state_school = parts[1]
                if len(state_school) >= 4:  # If the state and school part is at least 4 characters
                    state = state_school[:2]  # First two characters are the state
                    school = state_school[2:]  # The remaining characters are the school
                else:
                    state = "N/A"
                    school = "N/A"
            else:
                state = "N/A"
                school = "N/A"

            print(f"{idx + 1}. {file} - State: {state}, School: {school}")

    while True:
        # Prompt the user to select a file or exit
        file_index = input("\nSelect the Excel file by entering the number (or press 0 to exit): ")

        if file_index == '0':
            print("Exiting the program.")
            sys.exit()  # Exit the program

        try:
            file_index = int(file_index) - 1  # Convert to int and adjust for 0-based indexing

            if 0 <= file_index < len(files):
                selected_file = files[file_index]
                selected_file_path = os.path.join(folder_path, selected_file)
                # Extract the file prefix from the filename
                file_name = os.path.splitext(selected_file)[0]  # Remove the .xlsx extension
                file_prefix = file_name.split('_')[0]  # Assuming prefix is before the first underscore
                return selected_file_path, file_prefix
            else:
                print("Invalid selection. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def find_excel_file(base_path):
    current_path = base_path

    while True:
        # Check for Excel files in the current directory
        selected_file = list_excel_files(current_path)
        if selected_file:
            return selected_file

        # If no Excel files, check for subfolders
        selected_folder = list_folders(current_path)

        # If user chooses to go up, go to the parent directory
        if selected_folder == 'up':
            # If already at the base directory, we can't go up
            if current_path == base_path:
                print("Already at the top level.")
            else:
                current_path = os.path.dirname(current_path)  # Move up one level
        elif selected_folder:
            # If a folder is selected, move into it
            current_path = selected_folder
            selected_file = list_excel_files(current_path)

            # If Excel files were found, return the selected file
            if selected_file:
                return selected_file
        else:
            print("No folder selected. Try again.")


# Loop folder selection until an Excel file is found
selected_file = find_excel_file(base_path)
print(f"Selected file: {selected_file}")
