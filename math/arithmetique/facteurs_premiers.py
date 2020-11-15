# Guillaume Vanleene 2nd 9
# Script permettant l'affichage de facteurs communs sous forme de tableau ainsi que la réduction avec des puissances
# Doc disponible
# v 3.0

# Reflets :
# 1 - est_premier.py v2 : https://github.com/aodelta/python_utility/blob/main/math/is_prime.py

from math import sqrt

# Reflet 1
def est_premier(nombre):
    if nombre < 0 or nombre == 0:
        raise ValueError
    elif nombre == 1:
        return (False, None)
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

def reduire_en_puissance(diviseurs):
    diviseurs.sort()
    diviseurs_dictionnary_powers = {}
    for diviseur in diviseurs:
        if diviseur in diviseurs_dictionnary_powers:
            diviseurs_dictionnary_powers[diviseur] += 1
        else:
            diviseurs_dictionnary_powers[diviseur] = 1
    
    return diviseurs_dictionnary_powers


def facteurs_premiers(nombre_tab):
    if nombre_tab < 0 or nombre_tab == 0:
        raise ValueError
    elif nombre_tab == 1:
        return [(1, 1)]
    else:
        diviseurs = []
        while(True):
            (premier, diviseur) = est_premier(nombre_tab)
            diviseurs.append(int(diviseur))
            if not premier:
                nombre_tab /= diviseur
            else:
                break
        diviseurs_avec_puissance_dic = reduire_en_puissance(diviseurs)
        diviseurs_avec_puissance_tab = []
        for i, (nombre_tab, puissance_tab) in enumerate(diviseurs_avec_puissance_dic.items()):
            diviseurs_avec_puissance_tab.append([nombre_tab, puissance_tab])
        return diviseurs_avec_puissance_tab

def facteurs_premiers_calc():
    nombre_initial = None
    diviseurs = []

    print("Veuillez choisir le nombre à tester :")
    while(True):
        try:
            nombre_tab = int(input(" > "))
        except ValueError:
            print("Ceci n'est pas un chiffre")
            continue

        if nombre_tab < 0:
            print("Nombre négatif interdit")
            continue
        elif nombre_tab == 0:
            print("Division par zéro interdite")
            continue
        elif nombre_tab == 1:
            print("1 est fondamentalement premier")
            continue
        else:
            print("")
            nombre_initial = nombre_tab
            while(True):
                (premier, diviseur) = est_premier(nombre_tab)
                diviseurs.append(int(diviseur))
                if not premier:
                    nombre_tab /= diviseur
                else:
                    break

        taille_column_gauche = len(str(nombre_initial))

        nombre_gauche = None
        for i, nombre_tab in enumerate(diviseurs):
            nombre_droite = nombre_tab
            if i == 0:
                nombre_gauche = nombre_initial
            else:
                nombre_gauche = int(nombre_gauche / diviseurs[i - 1])
            
            if i != len(diviseurs) - 1:
                espace_requis = (taille_column_gauche - len(str(nombre_gauche))) * " "
                print("{0}{1} | {2}".format(espace_requis, int(nombre_gauche), int(nombre_droite)))
            else:
                espace_requis = (taille_column_gauche - len(str(nombre_droite))) * " "
                print("{0}{1} | -".format(espace_requis, int(nombre_droite)))


        diviseurs_avec_puissance_dic = reduire_en_puissance(diviseurs)
        diviseurs_avec_puissance_str = ""
        for i, (nombre_tab, puissance_tab) in enumerate(diviseurs_avec_puissance_dic.items()):
            exposant = ""
            if puissance_tab != 1:
                exposant = "^{0}".format(puissance_tab)
            if i == len(diviseurs_avec_puissance_dic) - 1:
                diviseurs_avec_puissance_str += "{0}{1}".format(nombre_tab, exposant)
            else:
                diviseurs_avec_puissance_str += "{0}{1} * ".format(nombre_tab, exposant)


        print("\n{0}\n".format(diviseurs_avec_puissance_str))
        diviseurs = []

if __name__ == "__main__":
    print("math/arithmetique/facteurs_premiers.py\n")
    facteurs_premiers_calc()