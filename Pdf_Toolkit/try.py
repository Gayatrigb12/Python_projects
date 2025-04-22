import PyPDF2
import os
from datetime import datetime

def merge_pdfs():
    output_dir = r"D:\PYTHON\Python_POC\Python_projects\Pdf_Merger\merged_files"
    os.makedirs(output_dir, exist_ok=True)

    try:
        count = int(input("Enter the number of PDF files to merge: "))
        if count < 2:
            print("You need at least 2 files to merge.")
            return
    except ValueError:
        print(" Invalid number entered.")
        return

    pdf_files = []
    for i in range(count):
        path = input(f" Enter path for file #{i + 1}: ").strip('"')
        if not os.path.exists(path):
            print(f" File not found: {path}")
            return
        pdf_files.append(path)

    merger = PyPDF2.PdfMerger()
    open_files = []

    try:
        for path in pdf_files:
            f = open(path, "rb")
            open_files.append(f)
            merger.append(f)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_path = os.path.join(output_dir, f"merged_{timestamp}.pdf")
        merger.write(output_path)
        print(f"Merged PDF saved at: {output_path}")
    finally:
        for f in open_files:
            f.close()
        merger.close()


def slice_pdf():
    output_dir = r"D:\PYTHON\Python_POC\Python_projects\Pdf_Merger\sliced_files"
    os.makedirs(output_dir, exist_ok=True)

    path = input("Enter the path of the PDF to slice: ").strip('"')
    if not os.path.exists(path):
        print(f" File not found: {path}")
        return

    try:
        start_page = int(input("Enter start page (starting from 1): ")) - 1
        end_page = int(input(" Enter end page (inclusive): "))
    except ValueError:
        print("Invalid page numbers.")
        return

    try:
        with open(path, "rb") as file:
            reader = PyPDF2.PdfReader(file)
            writer = PyPDF2.PdfWriter()

            if start_page < 0 or end_page > len(reader.pages) or start_page >= end_page:
                print("Invalid page range.")
                return

            for i in range(start_page, end_page):
                writer.add_page(reader.pages[i])

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            output_path = os.path.join(output_dir, f"sliced_{timestamp}.pdf")
            with open(output_path, "wb") as output_pdf:
                writer.write(output_pdf)

            print(f"Sliced PDF saved at: {output_path}")
    except Exception as e:
        print(f"Error slicing PDF: {e}")


# === Main Menu ===
print("***PDF TOOLKIT***")
print("1 Merge PDFs")
print("2 Slice PDF")
choice = input("Select an option (1 or 2): ").strip()

if choice == "1":
    merge_pdfs()
elif choice == "2":
    slice_pdf()
else:
    print(" Invalid choice.")
