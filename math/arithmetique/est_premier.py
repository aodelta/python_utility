# Guillaume Vanleene 2nd 9
# Script prenant un nombre et donnant son diviseur s'il n'est pas premier en retour en utilisant une racine carré arroundie (+ rapide)
# v 2.0
from math import sqrt

def est_premier(nombre):
    if nombre < 0 or nombre == 0:
        raise ValueError
    elif nombre == 1:
        return (True, None)
    else:
        nombre_sqrt_arroundi = round(sqrt(nombre))
        premier = True
        diviseur = nombre
        for i in range(2, nombre_sqrt_arroundi + 1):
            if nombre % i == 0:
                premier = False
                diviseur = i
                break

        return (premier, diviseur)

def est_premier_calc():
    print("Entrez un nombre :")
    while(True):
        try:
            nombre = int(input(" > "))
        except ValueError:
            print("Ceci n'est pas un chiffre")
            continue

        if nombre < 0:
            print("Nombre négatif interdit")
        elif nombre == 0:
            print("Division par zéro interdite")
        elif nombre == 1:
            print("1 est fondamentalement premier")
        else :
            nombre_sqrt_arroundi = round(sqrt(nombre))
            premier = True
            for i in range(2, nombre_sqrt_arroundi + 1):
                if nombre % i == 0:
                    print(nombre, "n'est pas premier. Il est divisible par", i)
                    premier = False
                    break

            if premier:
                print(nombre, "est premier")

if __name__ == "__main__":
    est_premier_calc()