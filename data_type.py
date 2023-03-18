#------------------------------Les types de données en Python----------------------------------

# 1. nombres: ---> entiers(int), nombres à virgules (flottants(float))
# 2. chaînes de caractères ---> (str)
# 3. booléens ---> True ou False
# 4. listes ---> (list)
# 5. tuples ---> (tuple)
# 6. ensembles ---> (set)
# 7. dictionnaires ---> (dict).. etc

# -----------------1. nombres:------------------------------#

age = 24
nombre = 10
# print(type(age)) # Sortie : <class 'int'>
# print(type(nombre)) # Sortie : <class 'int'>

# flottants ---> float
taille = 1.80
pi = 3.14
# print(type(taille)) # Sortie : <class 'float'>
# print(type(pi)) # Sortie : <class 'float'>


# -------------------# 2. chaînes de caractères ---> (str)----------------------------#


nom = 'Jean'
un_autre_nom = "Je m'appelle Pièrre"

# print(type(nom)) # Sortie : <class 'str'>
# print(type(un_autre_nom)) # Sortie : <class 'str'>
# print(nom)


# --------------------3. booléens ---> True ou False---------------------------#


x = True
y = False

# print(type(x)) # Sortie : <class 'bool'>
# print(type(y)) # Sortie : <class 'bool'>


# -------------------4. listes ---> (list)----------------------------#
 

liste = [1, 2, 3, 4, 5]
# print(type(liste)) # Sortie : <class 'list'>

# Afficher la taille de la liste
# print(len(liste)) # Sortie : 5

# Afficher le premier élément de la liste
# print(liste[0]) # Sortie : 1



# ------------------5. tuples ---> (tuple)-----------------------------#


tuple_1 = (1, 2, 3, 4, 5)
# print(type(tuple_1)) # Sortie : <class 'tuple'>

# Afficher la taille du tuple
# print(len(tuple_1)) # Sortie : 5


# Modifier le premier élément du tuple (ne fonctionne pas)
# tuple_1[1] = 10

# print(tuple_1) # Sortie : TypeError: 'tuple' object does not support item assignment


# ------------------6. ensembles ---> (set)-----------------------------#

# creer un ensemble
ensemble = {1, 2, 3, 4, 5}
# print(type(ensemble)) # Sortie : <class 'set'>

# Afficher la taille de l'ensemble
# print(len(ensemble)) # Sortie : 5


# ------------------7. dictionnaires ---> (dict)-----------------------------#

# creer un dictionnaire
dictionnaire = {'prenom': 'Jean', 'nom': 'Emmanuel', 'age': 30, 'taille': 1.80}
# print(type(dictionnaire)) # Sortie : <class 'dict'>

# Afficher les éléments du dictionnaire
# print(dictionnaire) # Sortie : {'prenom': 'Jean', 'nom': 'Emmanuel', 'age': 30, 'taille': 1.80}

# afficher les éléments du dictionnaire individuellement
# print(dictionnaire['prenom']) # Sortie : Jean
# print(dictionnaire['nom']) # Sortie : Emmanuel
# print(dictionnaire['age']) # Sortie : 30
# print(dictionnaire['taille']) # Sortie : 1.8

# ajouter un élément au dictionnaire
dictionnaire['pays'] = 'France'
# print(dictionnaire) # Sortie : {'prenom': 'Jean', 'nom': 'Emmanuel', 'age': 30, 'taille': 1.8, 'pays': 'France'}



# supprimer un élément du dictionnaire
del dictionnaire['pays']
# print(dictionnaire) # Sortie : {'prenom': 'Jean', 'nom': 'Emmanuel', 'age': 30, 'taille': 1.8}



# ------------------8. NoneType ---> (NoneType)-----------------------------#

# creer un NoneType
none_type = None
# print(type(none_type)) # Sortie : <class 'NoneType'>


# ------------------9. complex ---> (complex)-----------------------------#


# creer un complex
complex = 1 + 2j

print(type(complex)) # Sortie : <class 'complex'>

# Afficher la partie réelle du complex
# print(complex.real) # Sortie : 1.0

# Afficher la partie imaginaire du complex
print(complex.imag) # Sortie : 2.0

# Afficher la partie réelle et imaginaire du complex
print(complex) # Sortie : (1+2j)



# Les commentaires en Python

# ------------------10.Bonus-Les commentaires en Python -----------------------------#


# Ceci est un commentaire sur une ligne


""" 
Ceci est un commentaire 
sur plusieurs lignes
"""

