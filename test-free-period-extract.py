import camelot.io as camelot



tables = camelot.read_pdf('outputnew2.pdf' ,strip_text='0')
print(tables)
tables.export('free2.json', f='json', compress=True) # json, excel, html, markdown, sqlite
print(tables[0])
print(tables[0].parsing_report)
print(tables[0].to_json('free2.json')) # to_json, to_excel, to_html, to_markdown, to_sqlite
print(tables[0].df) # get a pandas DataFrame!