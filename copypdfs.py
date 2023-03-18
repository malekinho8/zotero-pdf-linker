#!/usr/bin/env python

import argparse
import os
import shutil

# Parse the command-line arguments
parser = argparse.ArgumentParser(description="Copy Zotero-managed PDFs to a specified folder.")
parser.add_argument("output_folder", help="the output folder where PDFs will be copied")
parser.add_argument("input_string", help="the string that contains the information for the PDF files")
args = parser.parse_args()

# Copy any available PDF files to the output folder
for line in args.input_string.split("\n"):
    if line.endswith(".pdf},"):
        filename = line.split("{")[1].split(",")[0] + ".pdf"
        if not os.path.isfile(os.path.join(args.output_folder, filename)):
            src_path = line.split(":")[1].split(":")[0].strip()
            dest_path = os.path.join(args.output_folder, filename)
            shutil.copy(src_path, dest_path)

print("Done!")
