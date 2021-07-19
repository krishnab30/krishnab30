import PyPDF2


template = PyPDF2.PdfFileReader(open('merged_pdf.pdf','rb'))
watermark = PyPDF2.PdfFileReader(open('wtr.pdf','rb'))
output_pdf = PyPDF2.PdfFileWriter()


for i in range(template.getNumPages()):
	pages = template.getPage(i)
	pages.mergePage(watermark.getPage(0))
	output_pdf.addPage(pages)



	with open ('watermarked_pdf','wb') as file:
		output_pdf.write(file)





