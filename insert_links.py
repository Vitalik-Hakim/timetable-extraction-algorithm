import json




with open('ALL_names.txt', 'r') as file:
    names = file.readlines()
    names = map(lambda s: s.strip(), names)
    



for name in names:
    name_d = name.replace(" ","-")
    png = ".png"
    name_d = name_d.lower()
    year = "https://raw.githubusercontent.com/vitalik-hakim/TABLES404/main/imgs/{}{}".format(name_d,png)



    with open('clean.json', 'r+') as file:
        data = json.load(file)
        # data['STUDENTS'].update(user)
        data['STUDENTS'][name][0]['0'] = year
        file.seek(0)
        json.dump(data, file, indent=4)
