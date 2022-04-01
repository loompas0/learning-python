# create a file in the current directory
# w for writing , r for reading , r+ for reading and writing , 
# a for appending
myFile = open ("./myfile.txt","w")
myData = open ("./data.csv","w")
# open a file for reading
# myFile = open ("./myfile.txt","r")
# open the file for append without overriding
# myFile = open ("./myfile.txt","a")
# open the file for read and write
myFile = open ("./myfile.txt","r+")
myFile.write("Bonjour Monsieur \n")
myData = open ("./data.csv","r+")
myData.write ("id,name,email")
myData.write ("\n")
myData.write ("1,Rémy,rb@gmail.com")
myData.write ("\n")
myData.write ("2,Lédicia,lb@yahoo.com")
myData.write ("\n")
# close the file
myFile.close()
myData.close()
# open the file for read
myFile = open ("./myfile.txt","r")
myData = open ("./data.csv","r")
# print (myData.read()) # this will read the entire file
print (myFile.read())
print ("----------------------")
# read line by line
# example in a loop
number: int = 0
for line in myData:
    print (f"{number} {line} ")
    number += 1
# to create a list of all the line use
# myFile.readlines
myData.close()
myFile.close()