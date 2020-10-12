# !DOC

# Guillaume Vanleene 2nd 9
# Script permettant l'affichage de facteurs communs sous forme de tableau ainsi que la réduction avec des puissances

from math import sqrt

# Simple fonction pour tester si le nombre donné est premier. Si vérifié, retourne True et son diviseur. Sinon, retourne False et le nombre donné.
def is_prime(number):
    if number == 1: # 1 est fondamentalement premier
        return (True, 1)
    if number <= 0:
        raise ValueError # On "lève" l'erreur classique de python pour une valeur incorret car ce n'est pas censé se produire

    number_sqrt_arround = round(sqrt(number)) # Récupérer la racine carré
    prime = True
    divisor = number # Si le nombre est premier, cela sera la valeur retournée
    for i in range(2, number_sqrt_arround): # Pour chaque nombre comprit entre 2 et la valeur arrondie de la racine carré du nombre d'entré
        if number % i == 0: # S'il peut être divisé (résultat de la division entier (= sans reste (= où le reste est égal à 0)))
            divisor = i # Le diviseur retourné devient i, le diviseur vérifié
            prime = False # Le nombre n'est donc pas premier
            break
    return (prime, divisor)

def reduce_with_power(diviseurs):
    diviseurs.sort() # On trie les diviseurs pour les avoir dans le bon ordre à la fin
    diviseurs_dictionnary_powers = {} # Dictionnaire contenant comme clé le nombre ciblé, et comme valeur la puissance
    for diviseur in diviseurs:
        if diviseur in diviseurs_dictionnary_powers: # Si le nombre est déjà enregistré (s'il a déjà une puissance)
            diviseurs_dictionnary_powers[diviseur] += 1 # On en rajoute une
        else:
            diviseurs_dictionnary_powers[diviseur] = 1 # Sinon, on la crée avec la valeur 1 (1 puissance, logique)

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
        print("") # On appelle la fonction print en lui donnant une chaîne de charactère vide pour passer une ligne
        initial_number = number
        while(True):
            (prime, divisor) = is_prime(number) # On test si number est premier
            diviseurs.append(int(divisor)) # Quoiqu'il arrive, on l'ajoute au diviseur en le convertissant en int (par précaution)
            if not prime: # S'il n'est pas premier, alors on peut recommencer la boucle pour chercher le prochain diviseur
                number /= divisor
            else: # S'il est premier
                break # On quitte la boucle

    # transforme tous les nombres entiers de la liste en string
    # (plus précisement, on crée une nouvelle chaîne de charactère identique à diviseurs,
    # on convertit les nombres un par un en str, puis on assigne le résultat à la variable diviseurs_str )
    diviseurs_str = [str(x) for x in diviseurs]



    # Le gros problème qu'on rencontre avec python, c'est que pour afficher quelque chose à l'écran, c'est avec la fonction print, et elle n'afiche qu'une ligne, rien de plus
    # 1er problème  : on ne peut pas faire de tableau, on peut en imiter un au mieux avec des | et des maths
    # 2eme problème : Etant donné que le nombre de gauche, quand il est écrit, correspond à un diviseur précédant, le premier étant le nombre initial, on doit se projeter
    #                   dans le tableau, une case en arrière, pour le récupérer avant qu'il soit divisé


    # Soluce 1er problème (1/2) : ajuster la taille du tableau pour bien placer les |, tout un travail de relationnel et de proportionnalité
    # On calcule d'abord la taille maximum de la colone de droite, qui est donc le plus grand nombre le nombre de départ
    # On doit pour connaître la taille d'un nombre le convertir en chaîne de charactère puis appeler la fonction len(), fonction "clé" de python toujours disponible
    #   à qui on donne en paramètre notre chaîne de charactère (ou un tableau par exemple), et elle nous renvoie sa taille, soit le nombre de lettres (ou d'élément pout un tableau)
    left_column_length = len(str(initial_number)) # La taille maximum des nombres de la colones de gauche est forcement celle du plus grand, celui d'origine

    # Le nombre de la colone de gauche, à assigner après (on crée la variable maintenant pou éviter de devoir la re-créer en permanance dans la boucle (+ performance))
    left_number = None
    for i, number in enumerate(diviseurs):  # Pour chaque élement dans la liste des diviseurs, on récupère sa valeur et son index
                                            # (valeur (number) = diviseur, index (i) = combient-ième élément dans la liste, sa position)
        right_number = number # Le nombre dans la colone de droite égal au diviseur actuel
        if i == 0: # Si c'est la première ligne du tableau
            left_number = initial_number # Le nombre de gauche est juste le nombre de départ
        else: # Sinon
            # On divise nous même le nombre de gauche (égal au précédant dans la boucle) par l'ancien diviseur en utlisant un index avec - 1 car on sait qu'il existait
            #   quelqu'un chose avant
            left_number = int(left_number / diviseurs[i - 1])
        
        # Soluce 1er problème (2/2) : on calcule l'espace requis pour que les | soit bien aligné, qui est égal à la taille max de la colone - la taille du nombre qu'on veut afficher
        if i != len(diviseurs) - 1: # Si ce n'est pas le dernier élément du tableau, la dernière ligne
            space_required = (left_column_length - len(str(left_number))) * " " # L'espace requis est calculé avec le nombre de gauche actuel (* un espace, pour l'avoir en string)
            print("{0}{1} | {2}".format(space_required, int(left_number), int(right_number))) # On écrit l'espace requis, le nombre, | , puis le diviseur
        else:
            space_required = (left_column_length - len(str(right_number))) * " " # L'espace requis est celui du nombre de droite, le dernier diviseur
            print("{0}{1} | -\n".format(space_required, int(right_number))) # Puisque dans ce cas le nombre de droite est à gauche, on écrit à droite un -, pour signaler que le nombre n'a pas de diviseur
        


    diviseurs_with_power_dic = reduce_with_power(diviseurs) # On récupère les puissances dans un dictionnaire (voir la définition de la fonction plus haut)
    diviseurs_with_power_str = ""
    for i, (number, power) in enumerate(diviseurs_with_power_dic.items()): # Pour chaque item du dictionnaire et son index
        exposant = "" # On créer une variable exposant vide (au cas où l'exposant serait de un)
        if power != 1: # Si la puissance n'est pas de une
            exposant = "^{0}".format(power) # On créer la chaîne de charactère adapté pour montrer l'exposant
        if i != len(diviseurs_with_power_dic) - 1: # Si ce n'est pas le dernier élément
            diviseurs_with_power_str += "{0}{1} * ".format(number, exposant) # On rajoute a la variable le nombre * sa puissance et un * pour le prochain nombre
        else:
            diviseurs_with_power_str += "{0}{1}".format(number, exposant) # On fait comme avant, mais sans le * car il n'y a rien après


    print("\n{0}\n".format(diviseurs_with_power_str)) # On écrit le tout avec des \n pour aller à la ligne, pour espacer le tout
    diviseurs = [] # On réinitialise le tableau des diviseurs, pour éviter les bugs lors de la prochaine entrée
