from pdf2image import convert_from_path
import textract
import os

single_pdfs_path = "single_pdfs/"

pdfs = os.listdir(single_pdfs_path)
print(pdfs)


for pdf in pdfs:
    if pdf == "imgs":
        pass
    else:
            
        print(single_pdfs_path,pdf)
        text = textract.process('{}{}'.format(single_pdfs_path,pdf), encoding='ascii')
        # print(text)
        with open('pdf-text.txt','wb') as f:
            f.write(text)


        # print only those lines starting with "IB"
        result = []
        def name_year_func():
            f = open("pdf-text.txt", 'r')
            s = f.readlines()
            for i in s:
                if 'IB' in i:
                    result.append(i.strip())
                    print(i)
                    break
                else:
                    continue
        name_year_func()

        print(result)
        result = "".join(result)

            # with open("name.txt", "r+") as fp:
            #     # access each line
            #     for line in fp:
            #         # check line number
            #         if i in lines:
            #             result.append(line.strip())
            #         i = i + 1
        with open('name_year','w') as g:
            g.write(str(result))


        with open('name_year','r') as g:
            result = g.readline()
            

        # result = list(result)
        print("resulte" , result )
        name_and_year = result

        name_and_year = name_and_year.split(" - ")
        print(name_and_year)

        name = name_and_year[1]
        year = name_and_year[0]

        name = name.strip()
        name = name.upper()
        # year = year.replace(".XLSX","")
        year = year.strip()
        # print("Year: "+ year, "Name: " + name)

        name_d = name.replace(" ","-")
        name_d = name_d.lower()
        imgs = single_pdfs_path + "imgs/"
        pdf_line = single_pdfs_path + pdf
        pages = convert_from_path(pdf_line, 0)
        page = pages[0]
        page.save(f"{imgs}{name_d}.png")
