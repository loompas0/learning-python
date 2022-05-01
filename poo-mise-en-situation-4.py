# POO EXERCICE DE MISE EN SITUATION 4

# ---
class Personne:
    def __init__(self, nom: str):
        self.nom = nom

    def SePresenter(self):
        print("Bonjour, je m'appelle " + self.nom)
#  ---
# creation liste de personnes
def creation_liste():
    index_Personne = 1
    nom_Persone = input ("nom de la personne " + str(index_Personne) + " : ")
    liste_Personne =[]
    while nom_Persone !="":
        liste_Personne.append(Personne(nom_Persone))
        index_Personne += 1
        nom_Persone = input ("nom de la personne " + str(index_Personne) + " : ")

    return liste_Personne
# ---
"""
noms = []
noms.append(input("nom de la personne 1 : "))
noms.append(input("nom de la personne 2 : "))
noms.append(input("nom de la personne 3 : "))

liste_de_Nom = []
"""
liste_de_Nom = creation_liste()
"""
for nom in noms:
    l.append(Personne(nom))
"""
for personne in liste_de_Nom:
    personne.SePresenter()