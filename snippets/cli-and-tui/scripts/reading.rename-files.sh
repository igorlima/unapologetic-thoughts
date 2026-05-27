#!/bin/bash
set -euo pipefail
#
# This script processes all PDF files in a specified directory by renaming them
# with a timestamp-based filename. The script iterates through each PDF file in
# the source directory, generates a new filename based on the current date and
# time, renames the file, and logs the operation. It ensures that files are
# processed sequentially with a 1-second delay between each operation. This can
# be useful for organizing files or preparing them for further processing.

read -p "Enter the folder to process (default: '~/Downloads/terminal-reading/pdf', use '.' for current folder): " pdf_dir
pdf_dir=${pdf_dir:-~/Downloads/terminal-reading/pdf}
# Expand ~ so glob patterns work correctly inside double-quoted strings
pdf_dir="${pdf_dir/#\~/$HOME}"

read -p "Enter the file extension to rename (default: 'pdf'): " ext
ext=${ext:-pdf}

# Process each file in the specified directory
for pdf_file in "$pdf_dir"/*.$ext; do
  # Skip if no matching files are found
  [ -e "$pdf_file" ] || continue
  # Generate a timestamp-based filename
  timestamp=$(date +"%Y-%m-%d_%H-%M-%S")
  new_filename="${timestamp}.${ext}"
  new_filepath="${pdf_dir}/${new_filename}"
  # Rename the file
  mv "$pdf_file" "$new_filepath"
  # Log the processed file
  echo "Processed: ${new_filename}"
  # Wait for 1 second before processing the next file
  sleep 1
done

: << 'END_COMMENT'
REFERENCE:
- ../python-llm-ai/gemini-pdf2md.py
- ~/workstation/git-remote-s3/s3-code-sketch/bash/scripts/reading.upload_pdfs_to_s3_with_confirm.sh
- ~/workstation/github/unapologetic-thoughts/snippets/cli-and-tui/scripts/reading.rename-files.sh
END_COMMENT
