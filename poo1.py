# Object Class Instance, method , Heritage, construct
# contruct in python def__init__ (param)
# For example
# Personne is an entity / class
# A personnne has data
#   name and age and size
# A personne can perform actions /method
#   ask_info and display_info
# Etre_Vivant <--- Parent Class
#   Chat <-- Child Class
#   Personne <-- Child Class
# Child Class will inherit method and vaiable from parent class
#
# ---- DEFINITION ---


class Etre_Vivant:  # class parent
    is_Human = False
    espece = "not defined"
    def affiche_Espece(self): # Class method
        print (f"Information être vivant : {self.espece}. ") #call variable at the class level

        # create contructor means create an object in memory and return it to self
    def __init__(self,name_Etre = "" ):
        self.name_Etre = name_Etre   # Create an 'instance' variable : name_Etre
        self.cm_ask_name()
        print ("fin constructeur " +self.name_Etre)

    def se_Presenter(self):     # INSTANCE method
        messagge_Etre = "Bonjour , je m'apppelle " + self.name_Etre
        print (f"{messagge_Etre} ")
        Etre_Vivant.affiche_Espece(self)

    def cm_ask_name (self):
        while  self.name_Etre == "":
            if self.is_Human:
                self.name_Etre = input("Quel est le nom de la personne ? ")
            else:
                self.name_Etre = input("Quel est le nom de l'animal' ? ")
    
    def other_Class_Method (): # CLASS method
        print ("none")


class Chat(Etre_Vivant):   # Chat-class will inherit from Etre_Vivant-class (in parentesis) 
    is_Human = False
    espece = "Chat (Mamifère Félins)" # class variable 

    # create contructor means create an object in memory and return it to self
    # inherit the def __init__() method from the parent class


class Personne(Etre_Vivant):
    # Class variable (not instance)
    is_Human = True
    espece = "Humain (Mamifère Homo Sapiens)" # class variable 
    # create contructor means create an object in memory and return it to self
    def __init__(self,name_Pers = "" ,age_Pers = 0,size_Pers = 0.0 , sex_Pers =""):
        self.name_Etre = name_Pers   # Create an 'instance' variable : name_Pers
        self.age_Pers = age_Pers
        self.size_Pers = size_Pers
        self.sex_Pers = sex_Pers
        self.cm_ask_name()
        print ("fin constructeur " +self.name_Etre)

    def se_Presenter(self):     # INSTANCE method
        messagge_Pers = "Bonjour , je m'apppelle " + self.name_Etre
        if self.age_Pers == 0:
            print (f"{messagge_Pers} ")
        else:
            print (f"{messagge_Pers} j'ai {self.age_Pers} ans  et je mesure {self.size_Pers} m")
            if self.cm_is_Majeur(): 
                    print ("Je suis majeur")
            else:
                print ("je suis mineur")
        Personne.affiche_Espece(self)
       

    def cm_is_Majeur(self):
        return self.age_Pers >= 18
"""
    def cm_ask_name (self):
        while  self.name_Pers == "":
            self.name_Pers = input("Quel est le nom de la personne ? ")
    
    def affiche_Espece(): # Class method
        print (f"Information être vivant : {Personne.espece}. ") #call variable at the class level

    def other_Class_Mtehod (): # CLASS method
        print ("none")
"""
class Etudiant(Personne):
    # create contructor means create an object in memory and return it to self
    def __init__ (self,name_Pers = "" ,age_Pers = 0,size_Pers = 0.0 , sex_Pers ="", etudes ="" ):
        super().__init__(name_Pers,age_Pers,size_Pers,sex_Pers)
        self.etudes = etudes
    def affiche_Etudes(self):
        print (f"Je suis en : {self.etudes} .")
    def se_Presenter(self):     # INSTANCE method
        super().se_Presenter() # call method of parent
        Etudiant.affiche_Etudes(self)
       

# --- Functions ---
def liste_Presentation(liste):
    for i in (liste):
        i.se_Presenter()
        print()

# ---- USAGE ----
# personne1 = Personne("Rémy",57,1.87,"M") # create a personne or instance of Personne's class
# personne2 = Personne("Ledi",47,1.77,"F") 
# liste_Personnes =[personne1,personne2] # create a list with multiple objects
# or create directly object in the list

liste_Personnes = [
    Personne("Rémy",57,1.87,"M"),
    Personne("Ledi",47,1.77,"F"),
    Personne("Julie")
    ]
liste_Personnes.append (Personne("Lea"))
liste_Presentation(liste_Personnes)

liste_Chats =[
    Chat("Tom"),
    Chat("Felix"),
    Chat("Jean-Luc"),
    Chat()
    ]
liste_Presentation(liste_Chats)
etre_Vivant = Etre_Vivant()
etre_Vivant.se_Presenter()

etudiant = Etudiant ("",19,1.77,"F","Ecole de Commerce")
etudiant.se_Presenter()


# liste_Personnes[1].se_Presenter()
# liste_Personnes[2].se_Presenter()
# personne3 = Personne()
# personne4 = Personne (age_Pers=17)
# personne1.se_Presenter() # instance method with access to self
# personne2.se_Presenter()
# personne3.se_Presenter()
# personne4.se_Presenter()


# print (Personne.is_Human) # Call to class variable
# print (personne1.name_Pers) # Call to instance variable
# Personne.other_Class_Mtehod () #Class method without access to self similar to function

