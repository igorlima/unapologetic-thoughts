#!/bin/bash
# The script processes all PDF files in a specified folder by converting each
# to markdown format using the `gemini-pdf2md.py` script and saves the results
# in an output directory.

PDF_DIR=~/Downloads/terminal-reading/pdf
OUTPUT_DIR=~/Downloads/terminal-reading/epub
for pdf_file in "$PDF_DIR"/*.pdf; do
  filename=$(basename "$pdf_file" .pdf)
  ./gemini-pdf2md.py -i "$pdf_file" -o "$OUTPUT_DIR"
  echo "Processed: ${filename}"
  sleep 5  # waits 5 seconds before processing the next file
done
