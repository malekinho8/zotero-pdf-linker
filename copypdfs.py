#!/usr/bin/env python

import argparse
import os
import shutil
import pyperclip
import re
from utils import *

# Set the default output directory
DEFAULT_OUTPUT_DIR = "/Users/malek8/My Drive (malek8@mit.edu)/chapter-mapper"

# Get input text from clipboard and remove line breaks
input_string = pyperclip.paste().replace("\n", "")

# Parse the command-line arguments
parser = argparse.ArgumentParser(description="Copy Zotero-managed PDFs to a specified folder.")
parser.add_argument("output_folder", help="the output folder, either a full absolute path or relative path, where PDFs will be copied to")
parser.add_argument("--output-dir", default=DEFAULT_OUTPUT_DIR, help="the directory where the output folder is located")
args = parser.parse_args()

# Determine the full path to the output folder
if os.path.isabs(args.output_folder):
    output_folder = args.output_folder
else:
    output_folder = os.path.join(args.output_dir, args.output_folder)

# Find all file paths using regex
file_paths = extract_pdf_paths(input_str=input_string)

# Copy any available PDF files to the output folder
for pdf in file_paths:
    filename = pdf.split(os.sep)[-1]
    if not os.path.isfile(os.path.join(output_folder, filename)):
        dest_path = os.path.join(output_folder, filename)
        shutil.copy(pdf, dest_path)
        print(f'{filename} successfully copied to {args.output_folder}...')
    else:
        print(f'{filename} already exists in {args.output_folder}!')

print("Done!")
