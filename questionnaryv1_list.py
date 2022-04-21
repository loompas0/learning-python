# LES COLLECTIONS : PROJET QUESTIONNAIRE
#
# Partez de ce code source pour réaliser la version 2 du projet questionnaire
#
#############################################################################
# FORMATION COMPLÈTE "DÉVELOPPEUR PYTHON"
# 
# Pour progresser en programmation et aller plus loin avec le langage Python,
# découvrez ma formation complète ici : 
# https://codeavecjonathan.com/formations.html
#############################################################################

def demander_Reponse (minimum, maximum):
    reponse_Str = input("Votre réponse entre "+ str(minimum) + " et "+ str(maximum) +" : " )
    try:
        reponse = int(reponse_Str)
        if minimum <= reponse <= maximum:
            return (reponse)
        print (f"Merci entrer un chiffre entre {minimum} et {maximum} ")
    except:
        print ("Erreur merci d'entrer un chiffre")
    return (demander_Reponse(minimum,maximum))


def poser_question(question):
    global score
    print("QUESTION")
    print("  " + question[0])
    for i in range (len(question[1])):
        print (f"       ({i+1}) , {question[1][i]} ")
    print()
    reponse = demander_Reponse (1, len(question[1]))
    if question[1][reponse-1] == question[2]:
        print("Bonne réponse")
        score += 1
    else:
        print("Mauvaise réponse")
        
    print()


def lancer_questionnaire (liste_de_questions):
    for i in liste_de_questions:
        poser_question (i)


score = 0

question1 =  (
    "Quelle est la capitale de la France ? ",("Marseille", "Nice", "Paris", "Nantes","Marseille"),"Paris"
)
question2 =  (
    "Quelle est la capitale de l'Italie ? ", ("Rome", "Venise", "Pise", "Florence"),"Rome"
)
question3 =  (
    "Quelle est la capitale de la Belgique ? ", ("Ansvers", "Bruxelles", "Bruges", "Liège"),"Bruxelles"
)



questionnnaire = [question1,question2,question3]

lancer_questionnaire (questionnnaire)


print("Score final :", score)
