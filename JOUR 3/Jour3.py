import os
import string

os.chdir("/Users/anto/Desktop/Advent of Code/Advent-of-Code/JOUR 3")


####PUZZLE 1
with open("input.txt", "r") as variable:
  contenu = variable.readlines()

alpha = []
for i in range(len(contenu)):
  texte = contenu[i].replace("\n","")
  mid = int(len(texte)/2)
  p1 = texte[0:mid]
  p2 = texte[mid:mid*2]

  for j in range(mid):
    if(p2.find(p1[j]) != -1):
      valeur = p1[j]

  alpha.append(valeur)

valeur = 0
for i in alpha:
  if (i.islower()):
    valeur =valeur + ord(i) - 96
  else:
    valeur = valeur + (ord(i) + 32 + 26)-96
print("SUM ITEM",valeur)

####PUZZLE 2

with open("input2.txt", "r") as variable:
  contenu2 = variable.readlines()

alpha = []
for i in range(0,len(contenu2),3):
  print(i)
  p1 = contenu[i].replace("\n","")
  p2 = contenu[i+1].replace("\n","")
  p3 = contenu[i+2].replace("\n","")
  print(p1," ",p2," ",p3)
