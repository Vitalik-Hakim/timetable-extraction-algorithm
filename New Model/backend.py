
## Import all tools and libraries for fastApi and local modules 
import re
from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
import json
from Prototype1 import main
# from names_dict import classroom_fullname
# from mapping import classroom_fullname, teachers_fullname


#Initialize FastAPI App
app = FastAPI()

# Add CORS allowed sites and local host for debugging
origins = [
    "http://localhost",
    "http://localhost:5000",
    "http://127.0.0.1:5500",
    "https://mysostimetable.web.app",
    "http://192.168.43.117:8080",
    "http://localhost:8080",
    "http://127.0.0.1:8080"

]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



### Open data with timetable and students names in their respective manner
 ############# Load JSON Data ###########
with open('file.json') as d:
    userdata = json.load(d)

## Using Regex find whether a schedule has time in it and remove it to prevent errors
def check4time(s):
    k = s[0]
    if k.isnumeric() == True:
        l = re.sub(f'{k}.*?\n', '', s)
        return l.strip()
    else:
        return s

# Define a function to read text file that contains students and return the names as words in a str

def readFile(fileName):
        fileObj = open(fileName, "r") #opens the file in read mode
        words = fileObj.read().splitlines() #puts the file into an array
        fileObj.close()
        return words

# db: List[User] = [
#     User(
#     id=UUID("259ecedd-5441-453b-ae29-1f91ace8dfa5"),
#     first_name="Abdul-Hakim",
#     last_name="Aremeyaw",
#     gender=Gender.male,roles=[Role.admin, Role.user] )
#     ,
#     User(
#     id=UUID("b5d68e27-a506-4289-8035-a99ec007a184"),
#     first_name="Farida",
#     last_name="Aremeyaw",
#     gender=Gender.female,roles=[Role.student, Role.user] )

# ]


## Create an endpoint for searching name and finding it for further processing
@app.get("/search/{student_name}")
async def root(student_name: str, request: Request):
    client_host = request.client.host
    # with open("Hits.txt","a") as f:
    #     f.write("\n" + client_host)
    key = student_name
    Period = main(key)
    if Period == "UNKNOWN":
        Period = "couldn't find your data"

    return Period

# Create a failsafes incase you need empty requests to the server
@app.get("/app/failsafe")
async def fail_safe2():
    return " "

@app.get("/")
async def fail_safe2():
    return "Nothing to see here "

@app.get("/process/{string_get}")
async def name_search(string_get: str):
    # print(string_get)
    
    string = string_get
    print(string)
    
    print("This is string_get",string_get)
    # string = string.split("\\n\\n")
    # string = string[1]
    conditions = [string == "FORMMEETING-REGISTRATION",string == "FORMMEETINGREGISTRATION"]
    if any(conditions):
        res = ["Form-Tutor","Form Meeting","Form Rooms"]
        final_res = "\n".join(res)
        print(final_res)
        return final_res
    elif string == "LUNCH BREAK":
        res = ["You","Lunch","Vortex"]
        final_res = "\n".join(res)
        print(final_res)
        return final_res
    elif string == "SNACK BREAK":
        res = ["Class Reps","Snack","Year Areas"]
        final_res = "\n".join(res)
        print(final_res)
        return final_res
    elif string == "Free Period":
        res = ["Free Period","Free Time","Anywhere"]
        final_res = "\n".join(res)
        print(final_res)
        return final_res
    elif string == "ASSEMBLY":
        res = ["Assembly","Assembly","MNH"]
        final_res = "\n".join(res)
        print(final_res)
        return final_res
    elif "GUIDANCE Clubs Personal Project Extended Essay" in string:
        res = ["Clubs","Guidance and Counselling","PP/EE"]
        final_res = "\n".join(res)
        print(final_res)
        return final_res
    elif string == "CAS":
        res = ["CAS","SA","MNH"]
        final_res = "\n".join(res)
        print(final_res)
        return final_res
    elif string == "EXTENDEDESSAY-PERSONALPROJECTMNH":
        res = ["Personal-Project","MNH","Extended Essay"]
        final_res = "\n".join(res)
        print(final_res)
        return final_res
    elif string == "GUIDANCEANDCOUNSELLINGKAEXTENDEDESSAY-PERSONALPROJECTMNH":
        res = ["Extended Essay","MNH","Personal Project"]
        final_res = "\n".join(res)
        print(final_res)
        return final_res
    elif string == "GUIDANCEANDCOUNSELLING":
        res = ["Extended Essay","MNH","Personal Project"]
        final_res = "\n".join(res)
        print(final_res)
        return final_res
    elif string == "EXTENDEDESSAYPERSONALPROJECTMNH":
        res = ["Personal Project","MNH","Extended Essay"]
        final_res = "\n".join(res)
        print(final_res)
        return final_res  
# EXTENDEDESSAYPERSONALPROJECTMNH
############ Lists ##############
    Teachers = ['JA-MT ','NAA ','AK ','CA ','HAM ','DA ','RH ','MD ','TO ','VE ','EAA ','SM ','NM ','JA ','EFV ','EE ','JK ','MC','MO ','ECT ','DS ','IS ','ED ','MT ','LS', 'SE ', 'EE-LEK ', 'REN-BAA-KA ', 'MT-EE ', 'KAD ',  'KB ', 'ABM ', 'SK ', 'DS ', 'GA ', 'MG ', 'SM ', 'EG', 'SC ', 'AAS ', 'JB ', 'PK ', 'LEK ','KA ','BAA ','REN ','GGH']
    Classrooms = ["MUS R ","AVR1 ","ER1 ","MR1 ","AVR2 ","ER2 ","MR2 ","ER3 ","MR3 ","ER4 ","MR4 ","HR1 ","HR2 ","HR3 ","MLR1 ","MLR2 ","MLR3 ","MLR4 ","AR ","ITL1 ","ITL2 ","GR ","GL ","PL ","BL ","CL ","GenLab ","MUSR"]
    Classes = ['GEO1 ', 'GEO2 ', 'GEO3 ', 'GEO4 ', 'GEO5 ', 'RS1 ', 'RS2 ', 'RS3 ', 'RS4 ', 'RS5 ', 'VA1 ', 'VA2 ', 'VA3 ', 'VA4 ', 'VA5 ', 'CHEM1 ', 'CHEM2 ', 'CHEM3 ', 'CHEM4 ', 'CHEM5 ', 'MATH STD1 ', 'MATH STD2 ', 'MATH STD3 ', 'MATH STD4 ', 'MATH STD5 ', 'ENG LANG ACQ1 ', 'ENG LANG ACQ2 ', 'ENG LANG ACQ3 ', 'ENG LANG ACQ4 ', 'ENG LANG ACQ5 ', 'GUIDANCE AND COUNSELLING ', 'DGN1 ', 'DGN2 ', 'DGN3 ', 'DGN4 ', 'ATL SKILLS1 ', 'ATL SKILLS2 ', 'ATL SKILLS3 ', 'ATL SKILLS4 ', 'ATL SKILLS5 ', 'AMH1 ', 'AMH2 ', 'AMH3 ', 'AMH4 ', 'AMH5 ', 'CLUBS ', 'MATH EXT1 ', 'MATH EXT2 ', 'MATH EXT3 ', 'MATH EXT4 ', 'MATH EXT5 ', 'ICT1 ', 'ICT2 ', 'ICT3 ', 'ICT4 ', 'ICT5 ', 'HIST1 ', 'HIST2 ', 'HIST3 ', 'HIST4 ', 'HIST5 ', 'ENG SUP1 ', 'ENG SUP2 ', 'ENG SUP3 ', 'ENG SUP4 ', 'ENG SUP5 ', 'PHY1 ', 'PHY2 ', 'PHY3 ', 'PHY4 ', 'PHY5 ', 'CAS ', 'EAL-ESL1 ', 'EAL-ESL2 ', 'EAL-ESL3 ', 'EAL-ESL4 ', 'EAL-ESL5 ', 'BIO1 ', 'BIO2 ', 'BIO3 ', 'BIO4 ', 'BIO5 ', 'ENG L-LIT1 ', 'ENG L-LIT2 ', 'ENG L-LIT3 ', 'ENG L-LIT4 ', 'ENG L-LIT5 ', 'ECONS1 ', 'ECONS2 ', 'ECONS3 ', 'ECONS4 ', 'ECONS5 ', 'FRE1 ', 'FRE2 ', 'FRE3 ', 'FRE4 ', 'FRE5 ', 'MUS1 ', 'MUS2 ', 'MUS3 ', 'MUS4 ', 'MUS5 ', 'MAA HL1 ', 'MAA HL2 ', 'MAA HL3 ', 'MAA HL4 ', 'MAA HL5 ', 'SP ab initio1 ', 'SP ab initio2 ', 'SP ab initio3 ', 'SP ab initio4 ', 'SP ab initio5 ', 'CS HL-SL1 ', 'CS HL-SL2 ', 'CS HL-SL3 ', 'CS HL-SL4 ', 'CS HL-SL5 ', 'EXTENDED ESSAY ', 'GEOG HL-SL1 ', 'GEOG HL-SL2 ', 'GEOG HL-SL3 ', 'GEOG HL-SL4 ', 'GEOG HL-SL5 ', 'PHY HL-SL1 ', 'PHY HL-SL2 ', 'PHY HL-SL3 ', 'PHY HL-SL4 ', 'PHY HL-SL5 ', 'CS HL1 ', 'CS HL2 ', 'CS HL3 ', 'CS HL4 ', 'CS HL5 ', 'PHY HL1 ', 'PHY HL2 ', 'PHY HL3 ', 'PHY HL4 ', 'PHY HL5 ', 'ENG A L-LITSL1 ', 'ENG A L-LITSL2 ', 'ENG A L-LITSL3 ','ENG A L-LITSL 3 ', 'ENG A L-LITSL4 ', 'ENG A L-LITSL5 ', 'ENG A LIT SL1 ', 'ENG A LIT SL2 ', 'ENG A LIT SL3 ', 'ENG A LIT SL4 ','ENG A L-LIT SL 4 ' ,'ENG A L-LIT SL 2 ','ENG A L-LIT SL 1 ','ENG A LIT SL5 ', 'TOK1 ', 'TOK2 ', 'TOK3 ', 'TOK4 ', 'TOK5 ', 'ECONS HL-SL1 ', 'ECONS HL-SL2 ', 'ECONS HL-SL3 ', 'ECONS HL-SL4 ', 'ECONS HL-SL5 ', 'FRE B SL1 ','FRE B SL3 ', 'FRE B SL4 ', 'FRE B SL5 ', 'CHEM HL1 ', 'CHEM HL2 ', 'CHEM HL3 ', 'CHEM HL4 ', 'CHEM HL5 ', 'CHEM SL1 ', 'CHEM SL2 ', 'CHEM SL3 ', 'CHEM SL4 ', 'CHEM SL5 ', 'ENG B HL1 ', 'ENG B HL2 ', 'ENG B HL3 ', 'ENG B HL4 ', 'ENG B HL5 ', 'BIO HL1 ', 'BIO HL2 ', 'BIO HL3 ', 'BIO HL4 ', 'BIO HL5 ', 'BIO SL1 ', 'BIO SL2 ', 'BIO SL3 ', 'BIO SL4 ', 'BIO SL5 ', 'AMH A1 SL1 ', 'AMH A1 SL2 ', 'AMH A1 SL3 ', 'AMH A1 SL4 ', 'AMH A1 SL5 ', 'SCA HL-SL1 ', 'SCA HL-SL2 ', 'SCA HL-SL3 ', 'SCA HL-SL4 ', 'SCA HL-SL5 ', 'HIST HL-SL1 ', 'HIST HL-SL2 ', 'HIST HL-SL3 ', 'HIST HL-SL4 ', 'HIST HL-SL5 ', 'FRE B HL-SL1 ', 'FRE B HL-SL2 ', 'FRE B HL-SL3 ', 'FRE B HL-SL4 ', 'FRE B HL-SL5 ', 'FRE B SL1 ', 'FRE B SL2 ', 'FRE B SL3 ', 'FRE BONS HL5 ', 'HIST HL1 ', 'HIST HL2 ', 'HIST HL3 ', 'HIST HL4 ', 'HIST HL5 ', 'ENG B HL1 ', 'ENG B HL2 ', 'ENG B HL3 ', 'ENG B HL4 ', 'ENG B HL5 ','DRA1 ','DRA‘1 ','DRA2 ','DRA3 ','DRA4 ','DRA5 ','ENG LI-LIT2 ','ENG ALILIT SL3 ','ENG ALILIT SL4 ','ENG ALILIT SL1 ','ENG ALILIT SL5 ','PHYHL-SL1','PHYHL-SL2','PHYHL-SL3','MATHEXT2','MATHEXT1','MATHEXT3','MATHEXT4','MATHEXT5','CS SUP1','SWA ab initio1','SWA ab initio2','SWA ab initio3','FRE B HL1','SWA B HL1','MAI SL1','HIST HL/SL1','MAA SL3','MAA SL2','MAA SL1','MAA SL4','GEOG HL2','GEOG HL1','GEOG HL3','VA HL/SL1','PHY HL/SL1','PHY HL/SL2','ECONS SL1','ECONS SL2','ECONS SL3','ECONS SL4','ENG A LIT HL1','ENG A LITHL1','SCA HL1','SCA HL2','SCA HL3','SCA HL/SL1','SCA HL/SL2','SCA HL/SL3']
    # class - room - teacher


    list_comp = Classes + Classrooms + Teachers
    # string_list = string.split("@@")
    print(string)
    new_list = []
    for i in Classes:
        i = i.strip()
        if i in string:
            new_list.append(i)
    for i in Classrooms:
        i = i.strip()
        if i in string:
            new_list.append(i)
    for i in Teachers:
        i = i.strip()
        if i in string:
            new_list.append(i)
    # print(classroom_fullname[new_list[1]])
    final_res = "\n".join(new_list)
    print("This is final res",final_res)
    

    return final_res
@app.get("/load/students")
async def load_students():
    students = readFile("Students.txt")

    print(students)
    
    return students