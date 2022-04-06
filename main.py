# Premier programme
your_Name = ""

while your_Name == "":
    your_Name = input ("Quel est votre nom ? ")
    if your_Name =="":
        print ("Erreur Votre nom ne peut être vide")

age_Str = ""
age_Num = 0

while age_Num <= 0:
    age_Str  = (input ("Quel age avez vous ? "))
    try:
        age_Num = int (age_Str) 
    except:
        print ("Erreur : vous devez entrer un nombre positif pour l'age , pas une chaine de caractère")
    else:
        age_Num = int (age_Str)
        if age_Num <= 0:
            print ("Erreur : vous devez entrer un nombre positif pour l'age , pas  négatif")

print("Vous vous appelez " + your_Name + ".")
print ("Vous avez " + str(age_Num) + " ans. ")
print ("L'an procahain vous aurez " + str(age_Num+ 1) + " ans. ")

