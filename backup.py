import os 
import shutil

source=input("Enter source Folder Name-")
destination=input("enter destination folder name-")

source=source+'/'
destination=destination+'/'

listoffiles=os.listdir(source)
for i in listoffiles:
    shutil.copy((source+i),destination)