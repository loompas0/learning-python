# Loop test
# syntax for list

names: list = ["Ledicia" , "Rémy", "Julie" , "Emma"]
# syntax for a set
telephones: set = { 388353911 , 685312249}
# syntax for dictionnaries 
persons :dict = {
    "first_name" : "Rémy",
    "last_name" : "Bernheim",
    "birth_date" : "June-30-1964",
    "age" : 54,
    "address" : "Rue Oberlin"
}
# syntax for a loop
for aname in names:
    print (aname)

# syntax for a while
number :int = 0
while number < 10:
    if number == 5:
        break

    print(f"the number is {number}")
    number += 1

else:
    print ("End of compute")

for aphone in telephones:
    print (str(aphone))

# for key in persons:
    # print (str(key) + " : " + str(persons[key]))
    # a more complex way to print
#    print (f"{key} : {persons[key]}")
print (persons.items())

# another way to loop
for key, value in persons.items():
    print (f"{key} : {value}")