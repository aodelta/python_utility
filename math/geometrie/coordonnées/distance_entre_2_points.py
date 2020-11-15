# Guillaume Vanleene 2nd 9
# Script permettant de connaître la distance entre 2 points donnés par coordonnés
# v 1.2

from math import sqrt, pow

# distance entre 2 coordonnées = sqrt( ( Xb - Xa )^2 + ( Yb - Ya )^2 )
def distance_entre_2_points(a_coordonnees, b_coordonnees):
    return round(sqrt(pow(b_coordonnees[0][0] - a_coordonnees[0][0], 2) + pow(b_coordonnees[0][1] - a_coordonnees[0][1], 2)), 3)

def demande_coordonnees(coordonnee_nom):
    print("Coordonnées du point {0} (x y): ".format(coordonnee_nom))

    # ( [x, y], nom )
    coordonnee = ([None] * 2, coordonnee_nom)

    while(True):
        user_input = input(" > ").split(" ")
        
        try:
            coordonnee[0][0] = int(user_input[0])
        except (ValueError, IndexError):
            print("Abscisse incorrect")
            continue
        try:
            coordonnee[0][1] = int(user_input[1])
        except (ValueError, IndexError):
            print("Ordonnée incorrecte")
            continue
        break
    return coordonnee

def distance_entre_2_points_calc():
    while(True):

        # On calcule la distance avec les coordonnées qu'on a demandé. Simple, compressé, et efficace
        distance = distance_entre_2_points(demande_coordonnees("A"), demande_coordonnees("B"))

        if distance < 0: # Erreur, une distance entre 2 points ne peut pas être négative
            print("\nLa distance est inférieure à 0 ? impossible : {0}\n".format(distance))
        else:
            print("\nLa distance est de", distance, "\n")

if __name__ == "__main__":
    distance_entre_2_points_calc()