# Guillaume Vanleene 2nd 9
# Script permettant de connaître la distance entre 2 points donnés par coordonnés
# v 1.1

def milieu_entre_2_points(a_coordonnées, b_coordonnées):
    return [round((a_coordonnées[0][0] + b_coordonnées[0][0]) / 2, 3), round((a_coordonnées[0][1] + b_coordonnées[0][1]) / 2, 3)]

def demander_coordonnees(coordonnee_nom):
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

        milieu = milieu_entre_2_points(demander_coordonnees("A"), demander_coordonnees("B"))
        
        print("\nLe mileu est de : ({0} ; {1})\n".format(milieu[0], milieu[0]))

if __name__ == "__main__":
    distance_entre_2_points_calc()