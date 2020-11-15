# Guillaume Vanleene 2nd 9
# Script permettant de savoir si un triangle est rectangle en lui donnant ses 3 longueurs
# v 1.0

# distances : [ ( distance, "pointpoint" ) ] * 3
def est_rectangle(longueurs):
    for i in range(3):
        if round(longueurs[i][0]**2) == round(longueurs[i-1][0]**2 + longueurs[i-2][0]**2): # Si la formule du théorême est vérifié
            for point_a in longueurs[i-1][1]: # On cherche le point commun à l'adjacent et à l'opposé, celui dont on dit que le triangle en est rectangle
                for point_b in longueurs[i-2][1]:
                    if point_a == point_b: # Quand il est trouvé (ne peux pas échouer)
                        return (True, point_a) # On retourne le tout (point_a ou point_b, c'est la même)
    
    return (False, None)

def demander_longueur(nom_longueur):
    print("Entrez la distance {0} :".format(nom_longueur))

    longueur = None

    while(True):
        try:
            longueur = int(input(" > "))
        except ValueError:
            print("Ceci n'est pas un nombre")
            continue

        if longueur < 0:
            print("Nombre négatif impossible")
        elif longueur == 0:
            print("Nombre null impossible")
        else :
            return (longueur, nom_longueur)

def est_rectangle_calc():
    (resultat, point_angle_droit) = est_rectangle([demander_longueur("AB"), demander_longueur("AC"), demander_longueur("BC")])

    if resultat:
        print("\nLe triangle est rectangle en {0}".format(point_angle_droit))
    else:
        print("\nLe triangle n'est pas rectangle en {0}".format(point_angle_droit))

if __name__ == "__main__":
    print("math/geométrie/triangles/est_rectangle.py\n")
    est_rectangle_calc()