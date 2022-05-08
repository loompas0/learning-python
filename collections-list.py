# Collections : (Tableaux=Array) , Listes , Tuples
# permet gestion de plusieurs éléments
# Tuple (): en lecture seule (RO) immuable
# Liste []: en lecture/écriture (RW) ajout/suppression  d'éléments
# utilisation de crochet pour indexation de l'élément

#      --- TUPLES ---
# personnes = ("Rémy","Lédicia","Julie","Emma")
# print (personnes)
# print (len(personnes))
# print (personnes[-2])
# print()

# for i in range(0,len(personnes)):
#    print (personnes[i])
# print()
# utilisation du Tuble comme paramètre de la boucle permet de parcourir les éléments du tuple
# for i in personnes:
#   print (i)
#    print(len(i))
#    print()
# valeurs = range(0,10))
# print (valeurs)
#    --- LISTES ---
"""personnes = ["Rémy","Lédicia","Julie","Emma"]
print (personnes)
nouvelle_Personne = "Tom"
personnes.append (nouvelle_Personne) # ajout d'un élément dans une liste
print (personnes)
del personnes[-2] # suppression avant denière personne
print (personnes)


#    --- FUNCTIONs and TUPLES ---
# function to return multiple values
def obtain_Info ():
    return ("Gil", 25 , 1.8)

def print_Info(name_p, age_p, size_p):
    print (f"Nom : {name_p}, Age : {age_p}, Taille : {size_p}m " )

# infos = obtain_Info()
# print (f"Nom : {infos[0]}, Age : {infos[1]}, Taille : {infos[2]}m " )
infos = obtain_Info()
print_Info(*infos)     # '*' allows to unpack the tuple
"""

#   --- SILCES ---
#  Applies to lists or tuples
personnes = ("Rémy","Lédicia","Julie","Emma","Gil","Laura","Stéphane")
for i in personnes [0:len(personnes):2]:   # slices = index debut et fin avec ':'
# [start:stop:step]
    print (i)

