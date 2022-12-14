# import the split pdf function
import os
from split_pdf import SPLIT_PDFS , SPLIT_PDFS_DIRTY
from extract import EXTRACT_CLEAN_DATA , EXTRACT_DIRTY_DATA
from replace_free_period import REPLACE_FREE_PERIODS  , FILL_IN_LUNCH
import shutil


# This function takes in the total number of pages of the pdf and the name of the pdf

# Lets find this data automatically

def extract_data():
    pdf_path = "raw_pdfs/"
    raw_pdfs = os.listdir(pdf_path)
    raw_pdf = pdf_path + raw_pdfs[0]
    print(raw_pdf[0])

    pdf_path_dotted = "raw_pdfs_dotted/"
    raw_pdfs_dotted = os.listdir(pdf_path_dotted)
    raw_pdf_dotted = pdf_path_dotted + raw_pdfs_dotted[0]
    print(raw_pdf_dotted[0])

    # # # # Split raw pdfs
    SPLIT_PDFS(raw_pdf)
    os.remove(raw_pdf)

    # # # # Split dirty pdfs
    SPLIT_PDFS_DIRTY(raw_pdf_dotted)
    os.remove(raw_pdf_dotted)




    # The second step is now done
    EXTRACT_CLEAN_DATA()
    shutil.rmtree('single_pdfs/')
    os.mkdir('single_pdfs/')
    # # Now lets extract the dotted pdf aka Dirty data
    EXTRACT_DIRTY_DATA()
    shutil.rmtree('single_pdfs_dotted/')
    os.mkdir('single_pdfs_dotted/')
    REPLACE_FREE_PERIODS()

    FILL_IN_LUNCH()

    original = r'json/clean.json' 
    target = r'final/clean.json' 

    shutil.move(original, target)









from tkinter import *
from tkinter import filedialog
file_list = []
def UploadAction(event=None):
    filename = filedialog.askopenfilename()
    file_list.append(filename) 
    target = r'raw_pdfs/' 
    shutil.move(filename, target)
    print('Selected:', filename)

def UploadAction2(event=None):
    filename = filedialog.askopenfilename()
    file_list.append(filename)
    target = r'raw_pdfs_dotted/' 
    shutil.move(filename, target)
    print('Selected:', filename)
def green_light():
    extract_data()

root = Tk()

root.title("TIMETABLE ALGORITHM GUI")
root.geometry("500x400")
button = Button(root, text='Upload Raw Timetable PDF', command=UploadAction, bg='lightgreen')
button.pack()
button2 = Button(root, text='Upload Dotted Timetable PDF', command=UploadAction2, bg='lightblue')
button2.pack()

button3 = Button(root, text='START CONVERSION`', command=green_light, bg='red')
button3.pack()
root.mainloop()









