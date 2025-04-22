import PyPDF2
from numpy.ma.core import append

pdf_files = ["D:/PYTHON/Python_POC/Python_projects/Pdf_Merger/pdf_Files/1.pdf", "D:/PYTHON/Python_POC/Python_projects/Pdf_Merger/pdf_Files/2.pdf"]
merger = PyPDF2.PdfMerger()

for pdf_file in pdf_files:
    pdf_file = open(pdf_file, "rb")
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    merger.append(pdf_reader)
pdf_file.close()
merger.write("merged.pdf")