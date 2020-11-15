# Guillaume Vanleene 2nd 9
# Script permettant de connaître le milieu entre 2 points donnés par coordonnés
# v 1.2

def milieu_entre_2_points(a_coordonnées, b_coordonnées):
    return [round((a_coordonnées[0][0] + b_coordonnées[0][0]) / 2, 3), round((a_coordonnées[0][1] + b_coordonnées[0][1]) / 2, 3)]

def demander_coordonnees(coordonnees_nom):
    print("Coordonnées du point {0} (x y): ".format(coordonnees_nom))

    # ( [x, y], nom )
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

def distance_entre_2_points_calc():
    while(True):

        milieu = milieu_entre_2_points(demander_coordonnees("A"), demander_coordonnees("B"))
        
        print("\nLe mileu est de : ({0} ; {1})\n".format(milieu[0], milieu[0]))

if __name__ == "__main__":
    print("math/geométrie/coordonnées/milieu_entre_2_points.py\n")
    distance_entre_2_points_calc()