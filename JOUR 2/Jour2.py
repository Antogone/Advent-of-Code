import os

os.chdir("/Users/anto/Desktop/Advent of Code/Advent-of-Code/JOUR 2")

with open("input.txt", "r") as variable:
  contenu = variable.readlines()

class Ligne:
    adv = 0
    moi = 0
    pts = 0

    def __init__(self,adv,moi,pts):  # Notre méthode constructeur
        self.adv = adv
        self.moi = moi
        self.pts = pts

    def modif_pts(self,adv,moi):
        self.moi = adv + moi

    def afficher_pouvoirs(self):
        print("Mon attribut est {0}.".format(self.pts))


Maléfique = \
    Ligne(input("Saisissez un nom : "),
          input("Saisissez les pouvoirs : "),
          input("Saisissez le film : "))


print(Maléfique.pouvoirs)
Maléfique.modif_pouvr("Water")
print(Maléfique.pouvoirs)

# print(dir(Maléfique)) => Renvoie une liste avec nom de methods et attr, renvoie tout ce qu'il y a dans l'obj
print(Maléfique.__dict__) # => Cet attribut est un dictionnaire qui contient en guise de clés les noms des attributs et, en tant que valeurs, les valeurs des attributs.

Maléfique.__dict__["pouvoirs"] = "Transformation dragon"
Maléfique.afficher_pouvoirs()

