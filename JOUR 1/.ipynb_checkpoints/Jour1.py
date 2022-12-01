import os

os.chdir("/Users/anto/Desktop/Advent of Code/Advent-of-Code/JOUR 1")

with open("input.txt", "r") as variable:
  contenu = variable.readlines()

elfe = []
valeur = 0
for i in range(len(contenu)):
    if contenu[i] == "\n" :
        elfe.append(valeur)
        valeur = 0
    else :
        valeur = valeur + int(contenu[i].replace("\n",""))

print("MAX CAL :",max(elfe))
print("TOP 3 : ",elfe[-1] + elfe[-2] +elfe[-3])
