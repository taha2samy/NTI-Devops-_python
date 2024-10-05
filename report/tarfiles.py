import tarfile
import os

def display_archive_contents(tar_filename):
    """Display the contents of the tar archive."""
    try:
        with tarfile.open(tar_filename, 'r') as tar:
            print("Contents of the archive:")
            tar.list()  # Lists the contents of the archive
    except FileNotFoundError:
        print(f"File {tar_filename} not found.")
    except tarfile.TarError as e:
        print(f"Error reading tar file: {e}")

def extract_files(tar_filename, extract_path):
    """Extract files from the tar archive to a specified path."""
    try:
        with tarfile.open(tar_filename, 'r') as tar:
            tar.extractall(path=extract_path)
            print(f"Extracted files to {extract_path}")
    except FileNotFoundError:
        print(f"File {tar_filename} not found.")
    except tarfile.TarError as e:
        print(f"Error extracting tar file: {e}")

def add_files_to_archive(tar_filename, file_paths):
    """Add files to an existing tar archive."""
    try:
        with tarfile.open(tar_filename, 'a') as tar:  # Open in append mode
            for file_path in file_paths:
                tar.add(file_path, arcname=os.path.basename(file_path))
            print(f"Added files to {tar_filename}")
    except FileNotFoundError:
        print(f"File {tar_filename} not found.")
    except tarfile.TarError as e:
        print(f"Error adding files to tar archive: {e}")

def main():
    tar_filename = input("Enter the path to the tar file: ")
    
    while True:
        print("\nMenu:")
        print("1. Display contents of the archive")
        print("2. Extract files to a specified path")
        print("3. Add files to the existing tar archive")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            display_archive_contents(tar_filename)
        elif choice == '2':
            extract_path = input("Enter the path to extract files to: ")
            extract_files(tar_filename, extract_path)
        elif choice == '3':
            # Get list of files to add
            file_paths = input("Enter the paths of files to add (comma-separated): ").split(',')
            file_paths = [file.strip() for file in file_paths]  # Clean up whitespace
            add_files_to_archive(tar_filename, file_paths)
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
