import os
import shutil
import datetime
import random
from pathlib import Path
 
my_dirs = [ Path("C:/Users/<Your UserName>/Desktop/IMG"),
            Path("C:/Users/<Your UserName>BUF5SGM/Desktop/PDF"),
            Path("C:/Users/<Your UserName>/Desktop/ZIP"),
            Path("C:/Users/<Your UserName>/BIN"),
            Path("C:/Users/<Your UserName>/Desktop/DOC"),
            Path("C:/Users/<Your UserName>/Desktop/DATASHEETS"),
            Path("C:/Users/<Your UserName>/Desktop/POWERPOINT"),
            Path("c:/Users/<Your UserName>/Desktop/3D"),
            Path("C:/Users/<Your UserName>/Desktop/OTHER")]
 
img = (".jpg", ".jpeg", ".jfif", ".pjpeg", ".pjp", ".png",
       ".gif", ".webp", ".svg", ".apng", ".avif")
   
pdf = ".pdf"
 
zip = ".zip"
 
bin = ".bin"
 
doc = (".docx", ".txt")
 
data = (".xlsx", ".csv", ".pbix")

pptx = ".pptx"
 
cad = ".stl"
 

def is_IMG(File): #Check File is IMG
    return os.path.splitext(File)[1]in img
 
def is_PDF(File): #Check if File is PDF
    return os.path.splitext(File)[1] == pdf
 
def is_ZIP(File): #Check if File is ZIP
    return os.path.splitext(File)[1] == zip
 
def is_BIN(File): #Check if File is BIN
    return os.path.splitext(File)[1] == bin
 
def is_DOC(File): #Check if File is DOC
    return os.path.splitext(File)[1] in doc
 
def is_DATA(File): #Check if File is DATA
    return os.path.splitext(File)[1] in data
 
def is_PPTX(File): #Check if File is PowerPoint
    return os.path.splitext(File)[1] == pptx
 
def is_3D(File): #Check if Files is 3D File
    return os.püath.splitext(File)[1] == cad
 

"""
 Function Checks if Directorys Exist and if not Creates them also returns Error if files could not be created
"""
def create_dirs():
    paths = len(my_dirs)
    for x in range(paths):
        if my_dirs[x].is_dir():
            print("Directory Exists")
        else:
            os.mkdir(my_dirs[x])
 
"""
If File with same Name Exists Rename it and Try again
"""
def ren_name(file,path):

    os.chdir("C:/Users/BUF5SGM/Downloads")
    #Generate Date to Add if Files with the same Name exist
    date = str(datetime.datetime.today())
    #Generate Random Number if File withe the Same Name exist
    r = random.randint(0,100)
 
    os.rename(file,str(r) + os.path.splitext(file)[0] + date.split(' ')[0] +  os.path.splitext(file)[1])
 
def mv_file():
    os.chdir("C:/Users/BUF5SGM/Downloads")
   
    while os.listdir():
        for file in os.listdir():
           
            if is_IMG(file):
                print("Image File")
                try:
                    shutil.move(file, my_dirs[0])
                except:
                    ren_name(file, my_dirs[0])
            elif is_PDF(file):
                print("PDF File")
                try:
                    shutil.move(file, my_dirs[1])
                except:
                    ren_name(file, my_dirs[1])
            elif is_ZIP(file):
                print("ZIP File")
                try:    
                    shutil.move(file, my_dirs[2])
                except:
                    ren_name(file, my_dirs[2])
            elif is_BIN(file):
                print("BIN File")
                try:
                    shutil.move(file, my_dirs[3])
                except:
                    ren_name(file, my_dirs[3])
            elif is_DOC(file):
                print("DOC File")
                try:
                    shutil.move(file, my_dirs[4])
                except:
                    ren_name(file, my_dirs[4])

            elif is_DATA(file):
                print("Data File")
                try:
                    shutil.move(file, my_dirs[5])
                except:
                    ren_name(file, my_dirs[5])
            elif is_PPTX(file):
                print("PowerPoint File")
                try:
                    shutil.move(file, my_dirs[6])
                except:
                    ren_name(file, my_dirs[6])
            elif is_3D(file):
                print("3D File")
                try:
                    shutil.move(file, my_dirs[7])
                except:
                    ren_name(file, my_dirs[7])
            else:
                print("Other File")
                try:
                    shutil.move(file, my_dirs[8])
                except:
                    ren_name(file, my_dirs[8])
 
def main():
   
    try:
        create_dirs()
    except:
        print("An Exception occurred while Creating the Directorys")
   
    try:
        mv_file()
    except:
        print("An Exception occurred while Moving the Files")
   
   
 
       
 
if __name__ == "_main_":
    main()