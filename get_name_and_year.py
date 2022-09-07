import textract

#, encoding='ascii'
text = textract.process('outputnew0.pdf', encoding='ascii')

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


# Rename File