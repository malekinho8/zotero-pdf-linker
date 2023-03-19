import re
import os

def extract_pdf_paths(input_str):
    # Define the regex pattern for matching file paths
    pattern = r'(?<=:)[^:]+(?=:application\/pdf)'

    # Use the findall() function from the re module to get all matches
    matches = re.findall(pattern, input_str)

    print(len(matches))

    file_paths = [x for x in matches if os.path.isabs(x)]

    return file_paths