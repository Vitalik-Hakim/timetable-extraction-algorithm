import json
link = "google.com"
# Now add it to the final file.json and add year group
    ########## Update STUDENTS #############
with open('ALL_names.txt', 'r') as file2:
    names = file2.readlines()
    names = map(lambda s: s.strip(), names)
with open('dirty.json', 'r+') as file1:
    data1 = json.load(file1)
for name in names:
    with open('clean.json', 'r+') as file:
        data = json.load(file)    
        # print(data['STUDENTS'][name][0]['0'])
        for i in range(1,6):
            # j = str(j)
            # print(data['STUDENTS'][name][0][i])
            for j in range(1,13):
                j = str(j)
                # print(data['STUDENTS'][name][i][j])
                # print(data1['STUDENTS'][name][i][j])
                if data1['STUDENTS'][name][i][j] == "FREE":
                    data['STUDENTS'][name][i][j] = "FREE"
                else:
                    print("NO FREE")
        file.seek(0)
        json.dump(data, file, indent=4)
