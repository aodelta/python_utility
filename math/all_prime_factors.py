# Guillaume Vanleene 2nd 9
# Script permettant l'affichage de facteurs communs sous forme de tableau ainsi que la réduction avec des puissances
from math import sqrt

def isPrime(number):
    if number == 1:
        return (True, 1)
    if number <= 0:
        raise "{0} is not a valid number".format(number)

    numberSqrtArround = round(sqrt(number)) + 1
    prime = True
    divisor = number # In case where the number is prime, we return it
    for i in range(2, numberSqrtArround + 1):
        if number % i == 0:
            divisor = i
            prime = False
            break
    return (prime, divisor)

def reduce_with_power(diviseurs):
    diviseurs.sort()
    diviseurs_with_powers = []
    diviseurs_dictionnary_powers = {}
    for diviseur in diviseurs:
        if diviseur in diviseurs_dictionnary_powers:
            diviseurs_dictionnary_powers[diviseur] += 1
        else:
            diviseurs_dictionnary_powers[diviseur] = 1

    for diviseur_keys in diviseurs_dictionnary_powers:
        diviseurs_with_powers += [[diviseur_keys, diviseurs_dictionnary_powers[diviseur_keys]]]
    
    return diviseurs_with_powers

displayMode = None
initalNumber = None
diviseurs = []

print("Mode d'affichage (1 par défaut) :")
print(" 1 - tableau 2*2")
print(" 2 - Affichage simple")

while(True):
    number = input(" > ")

    if number == "":
        displayMode = 1
        break
    else:
        try:
            number = int(number)
        except ValueError:
            print("Ceci n'est pas un chiffre")
            continue
        
        if number != 1 and number != 2:
            print("Vous devez choisir entre 1 et 2")
            continue
        
        else:
            displayMode = number
            break


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
        initalNumber = number
        while(True):
            (prime, divisor) = isPrime(number)
            diviseurs.append(int(divisor))
            if not prime:
                number /= divisor
            else:
                break
    break

# transfome tous les nombres entiers de la liste en string
diviseurs_str = [str(x) for x in diviseurs]

if displayMode == 2:
    print(" * ".join(diviseurs_str))

if displayMode == 1:
    left_column_length = len(str(initalNumber))


    left_number = None
    for i, number in enumerate(diviseurs):
        right_number = number
        if i == 0:
            left_number = initalNumber
        else:
            left_number = int(left_number / diviseurs[i - 1])
        
        space_required = (left_column_length - len(str(left_number))) * " "
        
        if i == len(diviseurs) - 1:
            space_required = (left_column_length - len(str(right_number))) * " "
            print("{0}{1} | -\n".format(space_required, int(right_number)))
        else:
            print("{0}{1} | {2}".format(space_required, int(left_number), int(right_number)))


diviseurs_with_power_arr = reduce_with_power(diviseurs)
diviseurs_with_power_str = ""
for i, diviseur in enumerate(diviseurs_with_power_arr):
    if i == len(diviseurs_with_power_arr) - 1:
        diviseurs_with_power_str += "{0}^{1}".format(diviseur[0], diviseur[1])
    else:
        diviseurs_with_power_str += "{0}^{1} * ".format(diviseur[0], diviseur[1])
print(diviseurs_with_power_str)