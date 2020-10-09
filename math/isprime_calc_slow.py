# Guillaume Vanleene 2nd 9
# Script prenant un nombre et donnant son diviseur s'il n'est pas premier en retour en boucle brute (lent)

while(True):
    try:
        number = int(input(" > "))
    except ValueError:
        print("Ceci n'est pas un chiffre")
        continue

    if number < 0:
        print("Nombre négatif interdit")
    if number == 0:
        print("Division par zéro interdite")
    if number == 1:
        print("1 est fondamentalement premier")
    else :
        prime = True
        for i in range(2, number):
            if number % i == 0:
                print(number, "n'est pas premier. Il est divisible par", i)
                prime = False
                break

        if prime:
            print(number, "est premier")
    