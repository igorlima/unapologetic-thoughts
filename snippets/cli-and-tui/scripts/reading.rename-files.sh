#!/bin/bash
#
# This script processes all PDF files in a specified directory by renaming them
# with a timestamp-based filename. The script iterates through each PDF file in
# the source directory, generates a new filename based on the current date and
# time, renames the file, and logs the operation. It ensures that files are
# processed sequentially with a 1-second delay between each operation. This can
# be useful for organizing files or preparing them for further processing.

PDF_DIR=~/Downloads/terminal-reading/pdf
# OUTPUT_DIR=~/Downloads/terminal-reading/epub

# Process each PDF file in the specified directory
for pdf_file in "$PDF_DIR"/*.pdf; do
  # Skip if no PDF files are found
  [ -e "$pdf_file" ] || continue
  # Generate a timestamp-based filename
  timestamp=$(date +"%Y-%m-%d_%H-%M-%S")
  new_filename="${timestamp}.pdf"
  new_filepath="${PDF_DIR}/${new_filename}"
  # Rename the PDF file
  mv "$pdf_file" "$new_filepath"
  # Log the processed file
  echo "Processed: ${new_filename}"
  # Wait for 1 seconds before processing the next file
  sleep 1
done

: << 'END_COMMENT'
REFERENCE:
- ../python-llm-ai/gemini-pdf2md.py
- ~/workstation/git-remote-s3/s3-code-sketch/bash/scripts/reading.upload_pdfs_to_s3_with_confirm.sh
END_COMMENT
