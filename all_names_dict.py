with open('dirty.json', 'r+') as file:
    data = json.load(file)
    data['STUDENTS'][name][i][j] = link_check
    # print(link_check)
    file.seek(0)
    json.dump(data, file, indent=4)


print([*data]['STUDENTS'])