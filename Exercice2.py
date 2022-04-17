# exercice table de multiplication
# creer une fonction qui permet d'afficher la table de multiplication
#
def verif_str (entree):
    entre = ""
    while type(entre) is not int:
        entre = input ("Merci d'entrer un chiffre pour le " + entree +" : ")
        try:
            entre = int(entre)
        except:
            entre = entre
        else:
            entre :int = int(entre)
    return (entre)


def saisir_Param ():    
    multipl = verif_str ("multiple")
    mini = verif_str ("minimum")
    maxi = verif_str ("maximmum") 
    while not (mini <= maxi):
        print ("le minimum doit être inférieur à maximum svp.")
        mini = verif_str ("minimum")
        maxi = verif_str ("maximmum") 
    return (multipl , mini , maxi ) 


def table_Multiplication (multiple, minim = 1, maxim = 10):
    print(f"Voici la table de {multiple} : ")
    for i in range(minim,maxim+1):
        result = (i)*multiple
        print (f"{i} x {multiple} = {result} ")

# main
(multipl , mini , maxi) = saisir_Param()
table_Multiplication (multipl, mini , maxi)
