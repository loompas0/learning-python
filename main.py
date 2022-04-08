# Premier programme
def demander_nom ():
    name_Str = ""

    while name_Str == "":
        name_Str = input ("Quel est votre nom ? ")
        if name_Str =="":
            print ("Erreur Votre nom ne peut être vide")
    return name_Str


def demander_age (person):
    age_Str = ""
    age_Int = 0

    while age_Int <= 0:
        age_Str  = (input (person + " Quel age avez vous ? "))
        try:
            age_Int = int (age_Str) 
        except:
            print ("Erreur : vous devez entrer un nombre positif pour l'age , pas une chaine de caractère")
        else:
            age_Int = int (age_Str)
            if age_Int <= 0:
                print ("Erreur : vous devez entrer un nombre positif pour l'age , pas  négatif")    
    return age_Int


def afficher (p_Name,p_Age):
    print()
    print("Vous vous appelez " + p_Name + ".")
    print ("Vous avez " + str(p_Age) + " ans. ")
    if p_Age < 10:
        print("vous êtes enfant")
    elif p_Age == 17:
        print ("Vous êtes preque majeur")
    elif p_Age == 18:
        print ("Félicitation vous venez d'être majeur")
    elif p_Age < 18:
        print ("Vous êtes mineur")
    elif p_Age <= 60:
        print ("vous êtes Majeur")
    else :
        print ("vous êtes Senior")
    print ("L'an procahain vous aurez " + str(p_Age+ 1) + " ans. ")

PEOPLE = 4
for index in range (0 , PEOPLE):
    your_Name = demander_nom()
    your_Age = demander_age(your_Name)
    afficher ( your_Name,your_Age )



# demande le nom
# your_Name1 = demander_nom()
# your_Name2 = demander_nom()
# demander l'age 
# age_Num1 = demander_age(your_Name1)
# age_Num2 = demander_age(your_Name2)

# afficher nom age et age + 1
# afficher (your_Name1,age_Num1)
# afficher (your_Name2,age_Num2)


