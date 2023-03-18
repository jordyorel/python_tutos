
# Les opérateurs avec python

# Opérateurs mathématiques: utilisés pour effectuer des opérations 
# mathématiques sur des valeurs numériques

# addition: +
# soustraction: -
# multiplication: *
# division: /
# modulo(reste de la division entière): %
# exponentiation(élévation à la puissance): **


a = 10
b = 3

print(a + b)   # Output: 13
print(a - b)   # Output: 7
print(a * b)   # Output: 30
print(a / b)   # Output: 3.3333333333333335
print(a % b)   # Output: 1
print(a ** b)  # Output: 1000


#----------------------------------------#


# Opérateurs de comparaison: permettent de comparer deux valeurs 
# et renvoient une valeur booléenne (True ou False) 
# en fonction du résultat de la comparaison.

# égal à: ==
# différent de: !=
# inférieur à: <
# supérieur à: >
# inférieur ou égal à: <=
# supérieur ou égal à: >=

a = 10
b = 3

print(a == b)  # Output: False
print(a != b)  # Output: True
print(a < b)   # Output: False
print(a > b)   # Output: True
print(a <= b)  # Output: False
print(a >= b)  # Output: True


#------------------------------------------#

# Opérateurs logiques: permettent de combiner des expressions booléennes

# ET logique: and
# OU logique: or
# NON logique: not

a = 10
b = 3
c = 5

print(a > b and b < c)   # Output: True
print(a < b or b > c)    # Output: False
print(not (a > b))        # Output: False




x = 10
if x > 0 and x < 100:
    print("x est entre 0 et 100")
else:
    print("x est en dehors de la plage")

# Sortie : "x est entre 0 et 100"


x = 10
if x < 0 or x > 100:
    print("x est en dehors de la plage")
else:
    print("x est entre 0 et 100")

# Sortie : "x est entre 0 et 100"



x = "pomme"
if x not in ["banane", "oranges", "fraise"]:
    print(f" Désolé nous n'avons plus de {x} en stoke")
    
# Output: "x is not a fruit we have in stock"



#------------------------------------------------#

# Opérateurs d'appartenance: permettent de vérifier 
# si un élément appartient à une séquence

# appartient à: in
# n'appartient pas à: not in

liste = [1, 2, 3, 4, 5]

print(2 in liste)        # Output: True
print(6 in liste)        # Output: False
print(2 not in liste)    # Output: False
print(6 not in liste)    # Output: True


# ------------------------------------------------#


# Opérateurs d'identité: permettent de comparer 
# si deux objets ont la même identité

# identique à: is 
# différent de: is not

a = 10
b = a
c = 5

print(a is b)       # Output: True
print(a is not c)   # Output: True
