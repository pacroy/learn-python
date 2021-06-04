#!/usr/bin/env python3
# pip install python-docx
import docx

def getText(filename):
    doc = docx.Document(filename)
    fullText = []
    for paragraph in doc.paragraphs:
        fullText.append(paragraph.text)
    return "\n".join(fullText)

print (getText("demo.docx"))
