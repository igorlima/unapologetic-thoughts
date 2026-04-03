#!/bin/bash
set -euo pipefail

# The script processes all PDF files in a specified folder by converting each
# to markdown format using the `gemini-pdf2md.py` script and saves the results
# in an output directory.

# Prompt the user for the delay between processing files
read -p "Enter the delay (in seconds) between processing each file (default: 1 second): " delay
# Set default delay to 1 second if no input is provided
delay=${delay:-1}

# Prompt the user for the extraction method used by gemini-pdf2md.py
read -p "Enter the extraction method (genai/docling, default: genai): " extraction_method
# Set default extraction method to genai if no input is provided
extraction_method=${extraction_method:-genai}

PDF_DIR=~/Downloads/terminal-reading/pdf
OUTPUT_DIR=~/Downloads/terminal-reading/epub
for pdf_file in "$PDF_DIR"/*.pdf; do
  filename=$(basename "$pdf_file" .pdf)
  ./gemini-pdf2md.py -i "$pdf_file" -o "$OUTPUT_DIR" --extraction-method "$extraction_method"
  echo "Processed: ${filename}"
  # Wait for the user-defined delay before processing the next file
  sleep "$delay"
done

: << 'END_COMMENT'
REFERENCE:
- ../python-llm-ai/gemini-pdf2md.py
- ~/workstation/git-remote-s3/s3-code-sketch/bash/scripts/reading.upload_pdfs_to_s3_with_confirm.sh
END_COMMENT
