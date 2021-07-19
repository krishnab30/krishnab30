import PyPDF2
import sys

#print(dir(PyPDF2))

input_pdfs = sys.argv[1:]

def pdf_merger(input_lists):
	merger = PyPDF2.PdfFileMerger()
	for pdfs in input_lists:
		print(pdfs)
		merger.append(pdfs)
	merger.write('merged_pdf.pdf')

pdf_merger(input_pdfs)
