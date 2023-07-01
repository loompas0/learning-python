# Les Fonctions

# Definition de la fonction

def input_Info(personne):
    name_Pers = input (f"What is your Name : {personne} ? ")
    age_Str = input (f"{name_Pers} {personne} what is your Age ? ")
#    if age_Str == "":
#        age_Pers = 0
#    else:
#        age_Pers = int(age_Str)
    try:
        pers0 = int(age_Str)
    except:
        pers0 = 0
    else:
        pers0 =int(age_Str)    
    return (name_Pers,pers0)

def est_Majeur(age_Personne):
    if age_Personne >= 18:
        return (True)
    return (False)

def print_Info (personne, name_Pers, adult_Pers , pers0 = 0 ):
    if name_Pers == "":
        print (f"Vous n'avez pas donné de nom pour {personne}, vous avez {pers0} ans ")
        return
    if pers0 == 0:
        print (f"Votre nom de {personne} est {name_Pers} et votre age n'est pas connu.")
    else:
        print (f"Votre nom de {personne} est {name_Pers} et vous avez {pers0} ans.")
    print (f"Le nom : '{name_Pers}' comporte {len(name_Pers)} caractères")
    if adult_Pers:
        print (f"{name_Pers} est majeur")
        return
    print (f"{name_Pers} est mineur")

def manipulation_Pers(pers_Num):
    info_Name, info_Age = input_Info(pers_Num)
    is_Adult = est_Majeur (info_Age)
    print_Info (pers_Num, info_Name, is_Adult, info_Age)


# Appeler une fonction

num_Pers = int (input("How many people , you want to enter ? "))
for i in range(num_Pers):
    manipulation_Pers(i+1)
# fin cours 2
# 
#
