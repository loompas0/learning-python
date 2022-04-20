# List Excercices   ask people Name
# ask many people name , infinite loop break when people name is empty
# at the end print all people name

def capitalize (name_P):
    name_C = name_P[0].upper() + name_P[1:len(name_P)]
    return (name_C)

def ask_People ():
    people_Name=""
    peoples = []
    while True:
        people_Name = input ("What is the people Name ? ")
        if people_Name == "":
            break
        people_Name = capitalize(people_Name)
        peoples.append (people_Name)
    return peoples

def display_People (people_List):
    pos = 0
    people_List.sort() # Alphabetic order in place
    print ("List of People in alphabetic order")
    for i in people_List:
        print (f" People Number {pos} Name {i}  ")
        pos += 1


list_of_people = ask_People()
display_People (list_of_people)
