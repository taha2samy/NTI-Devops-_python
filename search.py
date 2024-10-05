import os
import stat
from fuzzywuzzy import process

def get_permissions(filepath):
    """Retrieve the file permissions."""
    try:
        permissions = stat.filemode(os.stat(filepath).st_mode)
        return permissions
    except FileNotFoundError:
        return "File not found"

def search_files(directory, search_text, threshold):
    """Search for files in the specified directory."""
    matches = []
    
    # Walk through the specified directory
    for root, dirs, files in os.walk(directory):
        for filename in files:
            # Use FuzzyWuzzy to compare names
            match = process.extractOne(search_text, [filename])
            if match and match[1] >= threshold:  # Check if match meets the threshold
                file_path = os.path.join(root, filename)
                permissions = get_permissions(file_path)
                matches.append({'File': file_path, 'Permissions': permissions})
    
    return matches

# User input
directory = input("Enter the directory path to search in: ")
search_text = input("Enter the search text: ")
threshold = int(input("Enter the matching threshold (e.g., 70): "))

# Execute the search
results = search_files(directory, search_text, threshold)

# Print results
if results:
    print("Files found:")
    for result in results:
        print(f"{result['File']} - Permissions: {result['Permissions']}")
else:
    print("No matching files found.")
