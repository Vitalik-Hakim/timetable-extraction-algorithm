
import json

with open("dirty.json", "r") as json_file:

    dict = json.load(json_file)

names_list = list(dict['STUDENTS'].keys())
print(dict['STUDENTS'].keys())


for name in names_list:

    with open("All_names.txt","a") as f:
        f.write(name + "\n")

