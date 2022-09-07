# from PyPDF2 import PdfFileWriter, PdfFileReader


# input_pdf = PdfFileReader("Timetable.pdf")
# output = PdfFileWriter()
# totalpages = input_pdf.numPages

# print(str(totalpages) + "Pages")

# for page in range(0,5):
#     output.addPage(input_pdf.getPage(page))
#     page = str(page)
#     with open(f"page_{page}.pdf", "wb") as output_stream:
#         output.write(output_stream)


from PyPDF2 import PdfFileReader, PdfFileWriter


input_pdf = PdfFileReader("MYP_timetable_changesFINAL.pdf")
output = PdfFileWriter()
totalpages = input_pdf.numPages


for i in range(0,14):

    

    with open("MYP_timetable_changesFINAL.pdf", 'rb') as infile:

        reader = PdfFileReader(infile)
        writer = PdfFileWriter()
        writer.addPage(reader.getPage(i))

        with open(f'single_pdfs/outputnew{i}.pdf', 'wb') as outfile:
            writer.write(outfile)