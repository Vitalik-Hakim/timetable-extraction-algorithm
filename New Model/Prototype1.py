
import re
import time
import datetime
import calendar
import json
import pytz
tz = "Africa/Accra"
# day = 1
# period = '4'
# print(user['STUDENTS']['ABdul-mubs'][1][period])


def main(searched_user):
        
    with open('final_file.json', 'r+') as file:
        jsondata = json.load(file)
        name = "Abeiku Sam Armoo"
        # data['STUDENTS'].update(user)
        # print(data['STUDENTS'][name][0]['0'])
        file.seek(0)
        json.dump(jsondata, file, indent=4)


    # print(data)


    # Find if the name is in the database

    # read txt file 
    filetxt = open("Students.txt")

    data = filetxt.readlines()

    def searchName(name,text):
        name = name.upper()
        string = name
        # reversing words in a given string
        s = string.split()[::-1]
        l = []
        for i in s:
            # apending reversed words to l
            l.append(i)
        # printing reverse words
        r_name=" ".join(l)
        index = text.find(name)
        index2 = text.find(r_name)
        if (index >=0):
            return 1
        elif(index2>=0) :
            return 1
        else:
            return 0

    
    for i in data:
        if (searchName(searched_user,i)):
            key = i
            print(key)
            break
        else:
            key = "UNKNOWN"
            continue
    key = key.strip()
    students = "STUDENTS"
    print(key)



    period_one_start = 27000

    period_one_end = 28200

    period_two_start = 28200

    period_two_end = 30900

    period_three_start = 30900

    period_three_end = 33600

    period_four_start = 33600

    period_four_end = 34800

    period_five_start = 34800

    period_five_end = 37500

    period_six_start = 37500

    period_six_end = 40200

    period_seven_start = 40200

    period_seven_end = 42900

    period_eight_start = 42900

    period_eight_end = 45300

    period_nine_start = 45300

    period_nine_end = 48000

    period_ten_start = 48000

    period_ten_end = 50700

    period_eleven_start = 50700

    period_eleven_end = 53400

    period_twelve_start = 53400

    period_twelve_end = 56100






    # get time



    curr_time = jsondata[students][key][0]['1']
    print(curr_time)
    curr_time = curr_time.split("\n")



    def get_sec(time):
        secs = sum(int(x) * 60 ** i for i, x in enumerate(reversed(time.split(':'))))
        return secs

    # start_time = get_sec(curr_time[1]+":00")
    # end_time = get_sec(curr_time[2]+":00")

    get_now = str(datetime.datetime.now().time())
    print(get_now)
    now_list = get_now.split(".")
    now_time = now_list[0]
    curr_time1 = get_sec(now_time)

    curr_time1 =  53411


    print(curr_time1)

    # print(start_time,end_time)

    my_date = datetime.datetime.now(pytz.timezone(tz))
    today =calendar.day_name[my_date.weekday()]  #'Wednesday'




        #10
    if today == "today":
        today = 1
    elif today == "Tuesday":
        today = 2
    elif today == "Wednesday":
        today = 3
    elif today == "Thursday":
        today = 4
    elif today == "Friday":
        today = 5
    else:
        today = 1



    if key in jsondata[students]:
        # curr_time = int(curr_time)
        curr_time1 = int(curr_time1)


# 1 Period
        if curr_time1 in range(period_one_start,period_one_end):
            int_period = '1'

            second_period = str(int(int_period)+1)
            third_period = str(int(int_period)+2)
            fourth_period = str(int(int_period)+3)

            returned_period_one = jsondata[students][key][today][int_period]
            returned_period_two = jsondata[students][key][today][second_period]
            returned_period_three = jsondata[students][key][today][third_period]
            returned_period_four = jsondata[students][key][today][fourth_period]


            print(jsondata[students][key][today][int_period])
            print(jsondata[students][key][today][second_period])
            print(jsondata[students][key][today][third_period])
            print(jsondata[students][key][today][fourth_period])

            data_list = [returned_period_one,returned_period_two,returned_period_three,returned_period_four,period_one_end]
            # Return results
            return data_list 
# 2 Period
        elif curr_time1 in range(period_two_start,period_two_end):
            int_period = '2'

            second_period = str(int(int_period)+1)
            third_period = str(int(int_period)+2)
            fourth_period = str(int(int_period)+3)

            returned_period_one = jsondata[students][key][today][int_period]
            returned_period_two = jsondata[students][key][today][second_period]
            returned_period_three = jsondata[students][key][today][third_period]
            returned_period_four = jsondata[students][key][today][fourth_period]


            print(jsondata[students][key][today][int_period])
            print(jsondata[students][key][today][second_period])
            print(jsondata[students][key][today][third_period])
            print(jsondata[students][key][today][fourth_period])

            data_list = [returned_period_one,returned_period_two,returned_period_three,returned_period_four,period_two_end]
            # Return results
            return data_list 
# 3 Period
        elif curr_time1 in range(period_three_start,period_three_end):
            int_period = '3'

            second_period = str(int(int_period)+1)
            third_period = str(int(int_period)+2)
            fourth_period = str(int(int_period)+3)

            returned_period_one = jsondata[students][key][today][int_period]
            returned_period_two = jsondata[students][key][today][second_period]
            returned_period_three = jsondata[students][key][today][third_period]
            returned_period_four = jsondata[students][key][today][fourth_period]


            print(jsondata[students][key][today][int_period])
            print(jsondata[students][key][today][second_period])
            print(jsondata[students][key][today][third_period])
            print(jsondata[students][key][today][fourth_period])

            data_list = [returned_period_one,returned_period_two,returned_period_three,returned_period_four,period_three_end]
            # Return results
            return data_list 
# 4 Period
        elif curr_time1 in range(period_four_start,period_four_end):
            int_period = '4'

            second_period = str(int(int_period)+1)
            third_period = str(int(int_period)+2)
            fourth_period = str(int(int_period)+3)

            returned_period_one = jsondata[students][key][today][int_period]
            returned_period_two = jsondata[students][key][today][second_period]
            returned_period_three = jsondata[students][key][today][third_period]
            returned_period_four = jsondata[students][key][today][fourth_period]


            print(jsondata[students][key][today][int_period])
            print(jsondata[students][key][today][second_period])
            print(jsondata[students][key][today][third_period])
            print(jsondata[students][key][today][fourth_period])

            data_list = [returned_period_one,returned_period_two,returned_period_three,returned_period_four,period_four_end]
            # Return results
            return data_list 
# 5 Period
        elif curr_time1 in range(period_five_start,period_five_end):
            int_period = '5'

            second_period = str(int(int_period)+1)
            third_period = str(int(int_period)+2)
            fourth_period = str(int(int_period)+3)

            returned_period_one = jsondata[students][key][today][int_period]
            returned_period_two = jsondata[students][key][today][second_period]
            returned_period_three = jsondata[students][key][today][third_period]
            returned_period_four = jsondata[students][key][today][fourth_period]


            print(jsondata[students][key][today][int_period])
            print(jsondata[students][key][today][second_period])
            print(jsondata[students][key][today][third_period])
            print(jsondata[students][key][today][fourth_period])

            data_list = [returned_period_one,returned_period_two,returned_period_three,returned_period_four,period_five_end]
            # Return results
            return data_list 
# 6 Period
        elif curr_time1 in range(period_six_start,period_six_end):
            int_period = '6'

            second_period = str(int(int_period)+1)
            third_period = str(int(int_period)+2)
            fourth_period = str(int(int_period)+3)

            returned_period_one = jsondata[students][key][today][int_period]
            returned_period_two = jsondata[students][key][today][second_period]
            returned_period_three = jsondata[students][key][today][third_period]
            returned_period_four = jsondata[students][key][today][fourth_period]


            print(jsondata[students][key][today][int_period])
            print(jsondata[students][key][today][second_period])
            print(jsondata[students][key][today][third_period])
            print(jsondata[students][key][today][fourth_period])

            data_list = [returned_period_one,returned_period_two,returned_period_three,returned_period_four,period_six_end]
            # Return results
            return data_list 
# 7 Period
        elif curr_time1 in range(period_seven_start,period_seven_end):
            int_period = '7'

            second_period = str(int(int_period)+1)
            third_period = str(int(int_period)+2)
            fourth_period = str(int(int_period)+3)

            returned_period_one = jsondata[students][key][today][int_period]
            returned_period_two = jsondata[students][key][today][second_period]
            returned_period_three = jsondata[students][key][today][third_period]
            returned_period_four = jsondata[students][key][today][fourth_period]


            print(jsondata[students][key][today][int_period])
            print(jsondata[students][key][today][second_period])
            print(jsondata[students][key][today][third_period])
            print(jsondata[students][key][today][fourth_period])

            data_list = [returned_period_one,returned_period_two,returned_period_three,returned_period_four,period_seven_end]
            # Return results
            return data_list 
# 8 Period
        elif curr_time1 in range(period_eight_start,period_eight_end):
            int_period = '8'

            second_period = str(int(int_period)+1)
            third_period = str(int(int_period)+2)
            fourth_period = str(int(int_period)+3)

            returned_period_one = jsondata[students][key][today][int_period]
            returned_period_two = jsondata[students][key][today][second_period]
            returned_period_three = jsondata[students][key][today][third_period]
            returned_period_four = jsondata[students][key][today][fourth_period]


            print(jsondata[students][key][today][int_period])
            print(jsondata[students][key][today][second_period])
            print(jsondata[students][key][today][third_period])
            print(jsondata[students][key][today][fourth_period])

            data_list = [returned_period_one,returned_period_two,returned_period_three,returned_period_four,period_eight_end]
            # Return results
            return data_list 
# 9 Period
        elif curr_time1 in range(period_nine_start,period_nine_end):
            int_period = '9'

            second_period = str(int(int_period)+1)
            third_period = str(int(int_period)+2)
            fourth_period = str(int(int_period)+3)

            returned_period_one = jsondata[students][key][today][int_period]
            returned_period_two = jsondata[students][key][today][second_period]
            returned_period_three = jsondata[students][key][today][third_period]
            returned_period_four = jsondata[students][key][today][fourth_period]


            print(jsondata[students][key][today][int_period])
            print(jsondata[students][key][today][second_period])
            print(jsondata[students][key][today][third_period])
            print(jsondata[students][key][today][fourth_period])

            data_list = [returned_period_one,returned_period_two,returned_period_three,returned_period_four,period_nine_end]
            # Return results
            return data_list 
# 10 Period
        if curr_time1 in range(period_ten_start,period_ten_end):
            int_period = '10'

            second_period = str(int(int_period)+1)
            third_period = str(int(int_period)+2)
            # fourth_period = str(int(int_period)+3)

            returned_period_one = jsondata[students][key][today][int_period]
            returned_period_two = jsondata[students][key][today][second_period]
            returned_period_three = jsondata[students][key][today][third_period]
            # returned_period_four = jsondata[students][key][today][fourth_period]


            print(jsondata[students][key][today][int_period])
            print(jsondata[students][key][today][second_period])
            print(jsondata[students][key][today][third_period])
            # print(jsondata[students][key][today][fourth_period])
            empty = ""
            data_list = [returned_period_one,returned_period_two,returned_period_three,empty,period_ten_end]
            # Return results
            return data_list 
# 11 Period
        elif curr_time1 in range(period_eleven_start,period_eleven_end):
            int_period = '11'

            second_period = str(int(int_period)+1)
            # third_period = str(int(int_period)+2)
            # fourth_period = str(int(int_period)+3)

            returned_period_one = jsondata[students][key][today][int_period]
            returned_period_two = jsondata[students][key][today][second_period]
            # returned_period_three = jsondata[students][key][today][third_period]
            # returned_period_four = jsondata[students][key][today][fourth_period]


            print(jsondata[students][key][today][int_period])
            print(jsondata[students][key][today][second_period])
            # print(jsondata[students][key][today][third_period])
            # print(jsondata[students][key][today][fourth_period])
            empty = ""
            data_list = [returned_period_one,returned_period_two,empty,empty,period_eleven_end]
            # Return results
            return data_list 
# 12 Period
        elif curr_time1 in range(period_twelve_start,period_twelve_end):
            int_period = '12'

            # second_period = str(int(int_period)+1)
            # third_period = str(int(int_period)+2)
            # fourth_period = str(int(int_period)+3)

            returned_period_one = jsondata[students][key][today][int_period]
            # returned_period_two = jsondata[students][key][today][second_period]
            # returned_period_three = jsondata[students][key][today][third_period]
            # returned_period_four = jsondata[students][key][today][fourth_period]


            print(jsondata[students][key][today][int_period])
            # print(jsondata[students][key][today][second_period])
            # print(jsondata[students][key][today][third_period])
            # print(jsondata[students][key][today][fourth_period])
            empty = ""
            data_list = [returned_period_one,empty,empty,empty,period_twelve_end]
            # Return results
            return data_list 
        else:
            print("period not found")
            return "Couldn't find your period in the database!"
    else:
        print("user not found")
        return "Couldn't find your name in the database!"


    # print(jsondata[students][key]).
