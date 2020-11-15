# python_utility

Regroupement de beaucoup de fonctions pour calculatrice en python

## Installation sur calculatrice

### Ti-83 (Windows & MAC OS seulement)

> Liens rapides : [Windows](https://education.ti.com/download/en/ed-tech/13312F7CEC074A2DAFD7EE5646129839/3AECF615777A4BA7A566CA284C5DDEED/TIConnectCE-5.6.0.2082.exe) | [MAC OS](https://education.ti.com/download/en/ed-tech/68CEDD34FDC94622B4DBD173E6A0D8C3/53A0FBD756C04C2A9B67856A0966CD82/TIConnectCE-5.6.0.2082.dmg)

- Télécharger le logiciel Ti Connect via les liens rapides ou par https://education.ti.com/fr/products/computer-software/ti-connect-ce-sw

- L'installer en lancant l'executable (installez le driver/périphèrique que le logiciel tentera d'installer)

- Connecter sa calculatrice à son ordi (USB classique -> USB B)

- Procéder au déplacement des fichiers de votre ordinateur à votre calculatrie via le logiciel Ti Connect

## Vocab

### Reflets

Utilisation d'une fonction présente dans un autre fichier mais puisque l'import est quasi impossible sur une calculatrice, elle est réimplémenté dans le fichier en question.
Tout mise a jour du la fonction dans le fichier originel doit se répercuté dans tous les autres fichiers.
La version reflet doit être spécifiée.

### Version
Toutes versions de script est sous la forme suivante : **x**.**y**
Le **x** désigne la version de la fonction principale, ou de la logique derrière, l'algorithme
Le **y** désigne la version de l'implémentation dans le script, l'affichage ...
La version x doit toujours être a jour, car elle est mise ajour lors de bug majeur
La version y est réinitialisé lors de la maj de la version x