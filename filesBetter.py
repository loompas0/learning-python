# use with 
from fileinput import filename
import os.path # manipulate files 
fileName = "./mydata.csv"
fileExists = os.path.isfile (fileName) # return a bool is file exists
if fileExists:
    with open(fileName, "r") as myData: # another way of openning a file for read
        print (myData.read())
else:
    print (f"File {fileName} doesn't exists ")
    creation = input (" Enter (y or Y) to create: ")
    if creation.upper() == "Y":
        newFile = open (fileName,"w")
        newFile.write("Bonjour Monsieur \n")
        newFile.close()