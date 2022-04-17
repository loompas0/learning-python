
def print_Multiplication (n, min=1 ,max=10):
    if min > max :
        print (f"Erreur le minimum : {min} est supérieure au maximum : {max} ")
        return
    print(f"Table de multiplication de {n} :")
    for i in range( min , max+1 ):
        print (f"{i} x {n} = {i*n}")


print_Multiplication (7, 10,  1)

