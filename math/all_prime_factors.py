# Guillaume Vanleene 2nd 9
# Script permettant l'affichage de facteurs communs sous forme de tableau ainsi que la réduction avec des puissances
# Doc disponible

from math import sqrt

def is_prime(number):
    if number == 1:
        return (True, 1)
    if number <= 0:
        raise ValueError

    number_sqrt_arround = round(sqrt(number))
    prime = True
    divisor = number
    for i in range(2, number_sqrt_arround):
        if number % i == 0:
            divisor = i
            prime = False
            break
    return (prime, divisor)

def reduce_with_power(diviseurs):
    diviseurs.sort()
    diviseurs_dictionnary_powers = {}
    for diviseur in diviseurs:
        if diviseur in diviseurs_dictionnary_powers:
            diviseurs_dictionnary_powers[diviseur] += 1
        else:
            diviseurs_dictionnary_powers[diviseur] = 1
    
    return diviseurs_dictionnary_powers


initial_number = None
diviseurs = []

print("Veuillez choisir le nombre à tester :")
while(True):
    try:
        number = int(input(" > "))
    except ValueError:
        print("Ceci n'est pas un chiffre")
        continue

    if number < 0:
        print("Nombre négatif interdit")
        continue
    if number == 0:
        print("Division par zéro interdite")
        continue
    if number == 1:
        print("1 est fondamentalement premier")
        continue
    else:
        print("")
        initial_number = number
        while(True):
            (prime, divisor) = is_prime(number)
            diviseurs.append(int(divisor))
            if not prime:
                number /= divisor
            else:
                break
    
    diviseurs_str = [str(x) for x in diviseurs]

    left_column_length = len(str(initial_number))

    left_number = None
    for i, number in enumerate(diviseurs):
        right_number = number
        if i == 0:
            left_number = initial_number
        else:
            left_number = int(left_number / diviseurs[i - 1])
        
        if i != len(diviseurs) - 1:
            space_required = (left_column_length - len(str(left_number))) * " "
            print("{0}{1} | {2}".format(space_required, int(left_number), int(right_number)))
        else:
            space_required = (left_column_length - len(str(right_number))) * " "
            print("{0}{1} | -".format(space_required, int(right_number)))


    diviseurs_with_power_dic = reduce_with_power(diviseurs)
    diviseurs_with_power_str = ""
    for i, (number, power) in enumerate(diviseurs_with_power_dic.items()):
        exposant = ""
        if power != 1:
            exposant = "^{0}".format(power)
        if i == len(diviseurs_with_power_dic) - 1:
            diviseurs_with_power_str += "{0}{1}".format(number, exposant)
        else:
            diviseurs_with_power_str += "{0}{1} * ".format(number, exposant)


    print("\n{0}\n".format(diviseurs_with_power_str))
    diviseurs = []
