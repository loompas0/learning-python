from datetime import date
from ftplib import CRLF
from operator import le


class Person:
    def __init__(self, first_name, last_name, age, date_of_birth ) -> None:
        self.first_name: str = first_name
        self.last_name: str = last_name
        self.age: int = age
        self.date_of_birth: date = date_of_birth
    def walk(self):
        print(self.first_name + " is waklking... ")
    def speak(self):
        print ("Hello my name is " + self.last_name + " i am " + str (self.age) + "  years old")

remy = Person ('Rémy', 'Bernheim', 57, "June-30-1964")
ledicia = Person ('Lédicia', 'Bernheim', 47, "April-02-1974")

# print (remy.first_name + ' is ' + str(remy.age) + " years old")
remy.speak ()
remy.walk()

print ("------------------------------")

# print (ledicia.first_name + ' is ' + str(ledicia.age)+ " years old")
ledicia.speak()
ledicia.walk()


"""def print_id (person_identity):
     print ('le prénom est ' + person_identity.first_name )
     print ('le nom de famile est ' + person_identity.last_name )
     print ("l'age est : "  + str(person_identity.age ))
     print (person_identity.date_of_birth)

print_id (remy)
print (CRLF)
print_id (ledicia)
"""

