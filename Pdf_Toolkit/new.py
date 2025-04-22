import PyPDF2
import os
from datetime import datetime

# === Configuration ===
output_dir = r"D:\PYTHON\Python_POC\Python_projects\Pdf_Merger\merged_files"
os.makedirs(output_dir, exist_ok=True)

# === Input: Number of PDFs ===
try:
    count = int(input("📄 Enter the number of PDF files to merge: "))
    if count < 2:
        print("⚠️ You need at least 2 files to merge.")
        exit()
except ValueError:
    print("❌ Invalid number entered.")
    exit()

# === Input: File paths ===
pdf_files = []
for i in range(count):
    path = input(f"📥 Enter path for file #{i+1}: ").strip('"')
    if not os.path.exists(path):
        print(f"❌ File not found: {path}")
        exit()
    pdf_files.append(path)

# === Merge PDFs ===
merger = PyPDF2.PdfMerger()
open_files = []

try:
    for path in pdf_files:
        file = open(path, "rb")
        open_files.append(file)  # Store to close later
        merger.append(file)

    # Create filename with timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_path = os.path.join(output_dir, f"merged_{timestamp}.pdf")
    merger.write(output_path)
    print(f"✅ Merged PDF saved at: {output_path}")
finally:
    # Clean up: close all opened files
    for f in open_files:
        f.close()
    merger.close()
