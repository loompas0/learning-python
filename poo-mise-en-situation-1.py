# POO EXERCICE DE MISE EN SITUATION 1
# genre
#   False : Femme
#   True  : Homme
class Personne:
    def __init__(self, nom: str, age: int, genre: bool):
        self.nom = nom   # crée une variable d'instance : nom
        self.age = age
        self.genre = genre
        print("Constructeur personne " + self.nom)

    def SePresenter(self):
        # Bonjour, je m'appelle Jean, j'ai 30 ans
        # Je suis majeur
        masculin = self.cm_Ajouter_e()
        print("Bonjour, je m'appelle " + self.nom + ", j'ai " + str(self.age) + " ans")
        print( f"Genre : {masculin[1]}")
        if self.EstMajeur():
           print(f"Je suis majeur"+masculin[0])
        else:
            print("Je suis mineur"+masculin[0])
        print()

    def EstMajeur(self):
        return self.age >= 18

    def cm_Ajouter_e (self):
        if not self.genre:
            ajout_e = "e"
            sex = "Féminin"
        else :
            ajout_e =""
            sex = "Masculin"
        return (ajout_e,sex)
    def cm_Ajouter_Majeur (self):
        return


personne1 = Personne("Jean", 25, True)
personne1.SePresenter()

personne2 = Personne("Emilie", 17, False)
personne2.SePresenter()