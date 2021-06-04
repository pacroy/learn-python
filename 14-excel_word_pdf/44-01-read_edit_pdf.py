#!/usr/bin/env python3
# pip install PyPDF2
import PyPDF2

pdfFile = open("meetingminutes1.pdf", "rb")
reader = PyPDF2.PdfFileReader(pdfFile)
print(f"Number of pages: {reader.numPages}")

page = reader.getPage(0)
print(f"Page 1 content:\n{page.extractText()}")

# for pageNum in range(reader.numPages):
#     print(f"\n============================== {pageNum} ==============================")
#     print(reader.getPage(pageNum).extractText())
