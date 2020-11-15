# Guillaume Vanleene 2nd 9
# Script permettant de savoir si les 3 points donnés forment un triangle rectangle
# v 1.1

# Reflets :
# 1 - distance_entre_2_points.py v2 : https://github.com/aodelta/python_utility/blob/main/math/is_prime.py

from math import sqrt

# Reflet 1
def distance_entre_2_points(a_coordonnees, b_coordonnees):
    return round(sqrt(pow(b_coordonnees[0] - a_coordonnees[0], 2) + pow(b_coordonnees[1] - a_coordonnees[1], 2)), 3)

def est_triangle_rectangle(coordonnees):
    distances = [None] * 3

    for i in range(3): # Calcul des distances entre les 3 points
        distances[i] = distance_entre_2_points(coordonnees[i][0], coordonnees[i-1][0])

    for i in range(3): # Pour chaque point, vérifier si la distance qui lui est lié au carré est égal a la somme des deux autres au carré
        if(round(distances[i]**2) == round(distances[i-1]**2 + distances[i-2]**2)):
            return (True, coordonnees[i+1][1])
    return (False, None)

def demande_coordonnees(coordonnees_nom):
    print("Coordonnées du point {0} (x y): ".format(coordonnees_nom))

    # [ ( [x, y], nom ) ]
    coordonnees = ([None] * 2, coordonnees_nom)

    while(True):
        user_input = input(" > ").split(" ")
        
        try:
            coordonnees[0][0] = int(user_input[0])
        except (ValueError, IndexError):
            print("Abscisse incorrect")
            continue
        try:
            coordonnees[0][1] = int(user_input[1])
        except (ValueError, IndexError):
            print("Ordonnée incorrecte")
            continue
        break
    return coordonnees

def est_triangle_rectangle_calc():
    while(True):

        (resultat, point_angle_droit) = est_triangle_rectangle([demande_coordonnees("A"), demande_coordonnees("B"), demande_coordonnees("C")]);

        if resultat:
            print("\nLe triangle ABC est rectangle en {0}\n".format(point_angle_droit))
            
        else:
            print("Le triangle ABC n'est pas rectangle\n")

if __name__ == "__main__":
    print("math/geométrie/coordonnées/est_triangle_rectangle.py\n")
    est_triangle_rectangle_calc()