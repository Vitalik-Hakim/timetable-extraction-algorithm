
# Making it an exportable function into main

def SPLIT_PDFS(file_name):
    from PyPDF2 import PdfFileReader, PdfFileWriter
    input_pdf = PdfFileReader(f"{file_name}") # Replace this argument with the raw or dotted pf file name
    output = PdfFileWriter()
    totalpages = input_pdf.numPages


    for i in range(0,totalpages): # The last number is the number pages in the pdf

        with open(f"{file_name}", 'rb') as infile: # again replace with the filename

            reader = PdfFileReader(infile)
            writer = PdfFileWriter()
            writer.addPage(reader.getPage(i))

            with open(f'single_pdfs/outputnew{i}.pdf', 'wb') as outfile:
                writer.write(outfile)

def SPLIT_PDFS_DIRTY(file_name):
    from PyPDF2 import PdfFileReader, PdfFileWriter
    input_pdf = PdfFileReader(f"{file_name}") # Replace this argument with the raw or dotted pf file name
    output = PdfFileWriter()
    totalpages = input_pdf.numPages


    for i in range(0,totalpages): # The last number is the number pages in the pdf

        with open(f"{file_name}", 'rb') as infile: # again replace with the filename

            reader = PdfFileReader(infile)
            writer = PdfFileWriter()
            writer.addPage(reader.getPage(i))

            with open(f'single_pdfs_dotted/outputnew{i}.pdf', 'wb') as outfile:
                writer.write(outfile)