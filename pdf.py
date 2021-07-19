
import PyPDF2


#print(dir(PyPDF2))


with open('dummy.pdf',mode = 'rb') as f:
	reader = PyPDF2.PdfFileReader(f)
	pages = reader.getPage(0)
	pages.rotateClockwise(180)

	writer = PyPDF2.PdfFileWriter()
	writer.addPage(pages)

	with open('rot_pdf.pdf',mode = 'wb') as mod_file:
		writer.write(mod_file)
