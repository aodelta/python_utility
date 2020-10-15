# Guillaume Vanleene 2nd 9
# Script permettant de connaître la distance entre 2 points donnés par coordonnés
# v 1.0

from math import sqrt, pow

def distance_entre_2_points(A_coordonnées, B_coordonnées):
    return round(sqrt(pow(B_coordonnées[0] - A_coordonnées[0], 2) + pow(B_coordonnées[1] - A_coordonnées[1], 2)), 3)

def distance_entre_2_points_calc():
    while(True):
        A_coordonnées = [None] * 3
        B_coordonnées = [None] * 3

        print("Coordonnées du point A (x y): ")

        while(True):
            A_coordonnées[0] = input(" > ").split(" ")
                
            try:
                A_coordonnées[1] = int(A_coordonnées[0][0])
            except (ValueError, IndexError):
                print("Abscisse incorrect")
                continue
            try:
                A_coordonnées[2] = int(A_coordonnées[0][1])
            except (ValueError, IndexError):
                print("Ordonnée incorrecte")
                continue
            break

        print("Coordonnées du point B (x y): ")
        
        while(True):
            B_coordonnées[0] = input(" > ").split(" ")
            
            try:
                B_coordonnées[1] = int(B_coordonnées[0][0])
            except (ValueError, IndexError):
                print("Abscisse incorrect")
                continue
            try:
                B_coordonnées[2] = int(B_coordonnées[0][1])
            except (ValueError, IndexError):
                print("Ordonnée incorrecte")
                continue
            break

        distance = round(sqrt(pow(B_coordonnées[1] - A_coordonnées[1], 2) + pow(B_coordonnées[2] - A_coordonnées[2], 2)), 3)

        if distance < 0:
            print("La distance est inférieure à 0 ? :", distance)
            continue
        
        print("La distance est de", distance)

if __name__ == "__main__":
    distance_entre_2_points_calc()