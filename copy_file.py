import shutil
import os

def copy_files(source_directory, destination_directory, file_list):
    try:
        # Ensure the destination directory exists, create it if not
        os.makedirs(destination_directory, exist_ok=True)

        # Initialize a counter for the number of files copied
        files_copied_count = 0

        for file_name in file_list:
            source_path = os.path.join(source_directory, file_name)
            destination_path = os.path.join(destination_directory, file_name)

            # Check if the source file exists
            if not os.path.exists(source_path):
                print(f"Error: Source file '{source_path}' not found.")
                continue

            # Copy the file to the destination directory
            shutil.copy(source_path, destination_path)
            files_copied_count += 1
            print(f"File '{file_name}' copied successfully to '{destination_directory}'.")

        print(f"\n{files_copied_count} files copied successfully.")

    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
source_directory = r'your-path-here/'
destination_directory = r'your-path-here/'  
file_list = ['test.txt', 'test1.txt', 'test2.txt']  

copy_files(source_directory, destination_directory, file_list)
