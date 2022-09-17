




def REPLACE_FREE_PERIODS():
    import json

    with open("json/dirty.json", "r") as json_file:

        dict = json.load(json_file)

    names_list = list(dict['STUDENTS'].keys())
    print(dict['STUDENTS'].keys())

    for name in names_list:

        with open("processes/All_names.txt","a") as f:
            f.write(name + "\n")
    # Now add it to the final file.json and add year group
        ########## Update STUDENTS #############
    with open('processes/ALL_names.txt', 'r') as file2:
        names = file2.readlines()
        names = map(lambda s: s.strip(), names)
    with open('json/dirty.json', 'r+') as file1:
        data1 = json.load(file1)
    for name in names:
        with open('json/clean.json', 'r+') as file:
            data = json.load(file)    
            # print(data['STUDENTS'][name][0]['0'])
            for i in range(1,6):
                # j = str(j)
                # print(data['STUDENTS'][name][0][i])
                for j in range(1,13):
                    j = str(j)
                    # print(data['STUDENTS'][name][i][j])
                    # print(data1['STUDENTS'][name][i][j])
                    if data1['STUDENTS'][name][i][j] == ".":
                        data['STUDENTS'][name][i][j] = "FREE"
                    else:
                        print("NO FREE")
            file.seek(0)
            json.dump(data, file, indent=4)

def FILL_IN_LUNCH():
    import json
    with open('processes/ALL_names.txt', 'r') as file2:
        names = file2.readlines()
        names = map(lambda s: s.strip(), names)
    for name in names:
        with open('json/clean.json', 'r+') as file:
            data = json.load(file)    
            # print(data['STUDENTS'][name][i][j])
            # print(data1['STUDENTS'][name][i][j])
            for i in range(1,6):
                print(data['STUDENTS'][name][0]['8'],"here")
                data['STUDENTS'][name][i]['8'] = "LUNCH BREAK"
                data['STUDENTS'][name][i]['4'] = "SNACK BREAK"
            file.seek(0)
            json.dump(data, file, indent=4)
