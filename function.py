# A function is a group of statements to perfrom a certain task
# A function created using the def keyword then parentesis then colon then invoke it 
# using name of the function
# Parameters is what is in the entry of the function where using = you canput a default value
# Arguments is what is passed to the function between parenthesis when invoked
# A value or values could be returned by functions
def is_adult (age=0):
    if age >= 18 :
        print ("is an adult :) ")
        return (True)
    else:
        print ("is not yet an adult :( ")
        return(False)
# another simpler way to do the same in one line is : 
# def is_adult (age=0):
#    return if age >= 18 

def gender (aletter="Unknown"):
    if aletter.upper() == "M":
        return ("Male")
    elif aletter.upper() == "F":
        return ("Female")
    else: 
        return "Not knwon , needs to be M or F" 

print (gender("f"))
print (gender("m"))

def greet (aname, age=0 ):
    print (f"Welcome  {aname} , how are you doing?")
    print (f"You are {age} year old.")
greet("Julie",21)
greet("Emma",)
is_adult(17)

# Build in functions
# to define a function use def name ()
# to use a built in method it is used by putting a "." at the end
#  To import an external module within python use the keyword import
# example : import math
# second example: from math import sqrt (this will import a function with a module)
# 
